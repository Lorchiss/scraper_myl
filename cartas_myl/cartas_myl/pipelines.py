import os
from google.cloud import bigquery
from sqlalchemy.orm import sessionmaker
from cartas_myl.models import Carta, db_connect, create_table
from cartas_myl.bq import service_account_info, client


class CartasMylPipeline:

  def __init__(self):
    engine = db_connect()
    create_table(engine)
    self.Session = sessionmaker(bind=engine)

  def process_item(self, item, spider):
    session = self.Session()
    carta = Carta(**item)
    exist = session.query(Carta).filter_by(nombre=item['nombre'],
                                           edicion=item['edicion']).first()
    if not exist:
      try:
        session.add(carta)
        session.commit()
      except:
        session.rollback()
        raise
      finally:
        session.close()
    return item


class BigQueryPipeline(object):

  def __init__(self):
    self.client = client
    self.dataset_id = 'myl_fandom_com'
    self.table_id = 'cartas'

  def process_item(self, item, spider):
    # Aquí transformas el item de Scrapy en un formato adecuado para BigQuery
    row = {
        "nombre": item.get("nombre", ""),
        "tipo": item.get("tipo", ""),
        "fuerza": item.get("fuerza", ""),
        "coste": item.get("coste", ""),
        "raza": item.get("raza", ""),
        "frecuencia": item.get("frecuencia", ""),
        "edicion": item.get("edicion", ""),
        "habilidad": item.get("habilidad", "")
    }

    # Construye la consulta SQL para buscar datos existentes
    query = f"""
    SELECT *
    FROM `{service_account_info["project_id"]}.{self.dataset_id}.{self.table_id}`
    WHERE nombre = @nombre 
    AND tipo = @tipo
    AND fuerza = @fuerza
    AND coste = @coste
    AND raza = @raza
    AND frecuencia = @frecuencia
    AND edicion = @edicion
    AND habilidad = @habilidad
    """
    job_config = bigquery.QueryJobConfig(query_parameters=[
        bigquery.ScalarQueryParameter('nombre', 'STRING', row['nombre']),
        bigquery.ScalarQueryParameter('tipo', 'STRING', row['tipo']),
        bigquery.ScalarQueryParameter('fuerza', 'STRING', row['fuerza']),
        bigquery.ScalarQueryParameter('coste', 'STRING', row['coste']),
        bigquery.ScalarQueryParameter('raza', 'STRING', row['raza']),
        bigquery.ScalarQueryParameter('frecuencia', 'STRING',row['frecuencia']),
        bigquery.ScalarQueryParameter('edicion', 'STRING', row['edicion']),
        bigquery.ScalarQueryParameter('habilidad', 'STRING', row['habilidad'])
    ])

    # Ejecuta la consulta
    query_job = client.query(query, job_config=job_config)
    results = query_job.result()

    # Comprueba si se han devuelto filas
    rows = list(results)
    if rows:
      print("Los datos ya existen en la tabla.")
    else:
      print("Los datos no existen. Insertando...")
      # Insertar en BigQuery
      table_ref = self.client.dataset(self.dataset_id).table(self.table_id)
      table = self.client.get_table(table_ref)
      errors = self.client.insert_rows_json(table, [row])

      if errors != []:
        print("Errores al insertar en BigQuery:", errors)

      else:
        print("Datos insertados en BigQuery.")

    return item
