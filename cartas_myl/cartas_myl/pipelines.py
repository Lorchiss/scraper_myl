from sqlalchemy.orm import sessionmaker
from cartas_myl.models import Carta, db_connect, create_table

class CartasMylPipeline:
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        
    def process_item(self, item, spider):
        session = self.Session()
        carta = Carta(**item)
        exist = session.query(Carta).filter_by(nombre=item['nombre'], edicion=item['edicion']).first()
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
