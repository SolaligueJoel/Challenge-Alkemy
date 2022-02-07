from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from decouple import config
import logging

DATABASE_URI = config('BASE_DIR')
engine = create_engine(DATABASE_URI)
base = declarative_base()


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('clases.log')
fh.setFormatter(f)

logger.addHandler(fh)

logger.debug('Creando tabla en base de datos postgres...')

class Datos_argentina(base):
    __tablename__ = 'datos_argentina'
    id = Column(Integer, primary_key=True)
    cod_localidad = Column(Integer)
    id_provincia = Column(Integer)
    id_departamento = Column(Integer)
    categoria = Column(String)
    provincia = Column(String)
    localidad = Column(String)
    nombre = Column(String)
    domicilio = Column(String)
    codigo_postal = Column(String)
    numero_de_telefono = Column(String)
    mail = Column(String)
    web = Column(String)
    fecha_de_carga = Column(DateTime)       
    
    def __rpr__(self):
        return f"""Nombre:{self.nombre}\nProvincia:{self.provincia} """


class Datos_totales(base):
        __tablename__ = 'datos_totales'
        registro_categoria = Column(Integer, primary_key=True)
        registros_fuente = Column(Integer)
        registros_prov_cat = Column(Integer)
        fecha_de_carga = Column(DateTime)


class Datos_cine(base):
        __tablename__ = 'datos_cines'
        id = Column(Integer,primary_key=True)
        provincia = Column(String)
        cantidad_pantallas = Column(Integer)
        cantidad_espacios_incaa = Column(String)
        fecha_de_carga = Column(DateTime)


def create_schema():
        try:
                base.metadata.drop_all(engine)
                base.metadata.create_all(engine)
                logger.info('Tablas creadas correctamente!')
        except:
                logger.error('Error al crear las tablas.') 



