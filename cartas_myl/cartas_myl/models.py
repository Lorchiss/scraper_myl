from sqlalchemy import Column, Integer, String, create_engine, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Carta(Base):
    __tablename__ = 'cartas'

    id = Column(Integer, primary_key=True)
    nombre = Column('nombre', String())
    tipo = Column('tipo', String())
    fuerza = Column('fuerza', String())
    coste = Column('coste', String())
    raza = Column('raza', String())
    frecuencia = Column('frecuencia', String())
    edicion = Column('edicion', String())
    habilidad = Column('habilidad', String())

    # Creamos la constraint para la clave única
    __table_args__ = (UniqueConstraint('nombre', 'edicion', name='_nombre_edicion_uc'),)

    def __repr__(self):
        return f"<Carta(nombre='{self.nombre}', edicion='{self.edicion}', tipo='{self.tipo}')>"


def db_connect():
    engine = create_engine('sqlite:///myl.db')
    return engine

def create_table(engine):
    Base.metadata.create_all(engine)