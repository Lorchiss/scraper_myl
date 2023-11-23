import os
import json
from google.oauth2 import service_account
from google.cloud import bigquery

if os.environ.get("type") is not None:
    # Construye el diccionario de la cuenta de servicio desde las variables de entorno
    service_account_info = {
        "type": os.environ["type"],
        "project_id": os.environ["project_id"],
        "private_key_id": os.environ["private_key_id"],
        "private_key": os.environ["private_key"],
        "client_email": os.environ["client_email"],
        "client_id": os.environ["client_id"],
        "auth_uri": os.environ["auth_uri"],
        "token_uri": os.environ["token_uri"],
        "auth_provider_x509_cert_url": os.environ["auth_provider_x509_cert_url"],
        "client_x509_cert_url": os.environ["client_x509_cert_url"]
    }

    # Algunos de estos valores, como la clave privada, pueden necesitar ser procesados para reemplazar
    # secuencias de escape, por ejemplo, los saltos de línea.
    service_account_info["private_key"] = service_account_info[
        "private_key"].replace('\\n', '\n')
    
else:
    with open(r'C:\Users\fabia\dev\myl\cartas_myl\cartas_myl\scraping-349919-213c0506e5b7.json', 'r') as file:
        service_account_info = json.load(file)

#Convierte el diccionario en un objeto de credenciales
credentials = service_account.Credentials.from_service_account_info(
        service_account_info)
# Ahora, puedes usar estas credenciales para crear un cliente de BigQuery
client = bigquery.Client(credentials=credentials,
                         project=credentials.project_id)
