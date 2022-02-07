from asyncio.log import logger
import psycopg2
from config import config
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('db.log')
fh.setFormatter(f)

logger.addHandler(fh)

logger.debug('Realizando conexion con base la base de datos...')
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        logger.info('Conectando con PostgreSQL database...')
        conn = psycopg2.connect(**params)

        logger.info('Conecccion exitosa!')
    except (Exception, psycopg2.DatabaseError) as error:
        logger.critical(error)
    finally:
        if conn is not None:
            conn.close()
            logger.info('Database connection closed.\n')

