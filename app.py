from distutils.debug import DEBUG
from clases import engine,create_schema
import pandas as pd
import requests
from io import StringIO
from datetime import datetime
import pytz
import os
from datos import *
from db import connect
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('app.log')
fh.setFormatter(f)

logger.addHandler(fh)

logger.debug('Comenzando el proyecto...')

def nombre_ruta(data):
    time1 = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))
    to_csv_data = time1.strftime(f'{data}\\%Y-%B\{data}-%d-%m-%Y.csv')
    return to_csv_data
 

#Buscar la ruta del csv para luego poder leerlo
def buscar_csv(data_cultural):
    for file in os.listdir():
        if file.startswith(f'{data_cultural}'):
            return file
 
                
#Limpiar archivos csv, para cargar los nuevos.
def clean_csv():
    try:

        for file in os.listdir():
                if file.endswith('.csv'):
                    os.remove(file)
        logger.info('Archivos eliminados correctamente.')
    except Exception:
        logger.error('Error al eliminar los archivos csv.')


def fill(url_data,csv_data):
    r = requests.get(url_data).text
    c=pd.read_csv(StringIO(r),encoding='utf-8')
    data = nombre_ruta(csv_data)
    archivo_csv = c.to_csv(data,index=False,encoding='utf-8')
    return archivo_csv


def fill_csv():
    listaaa = ['museo','cine','biblioteca_popular']
    lista_url = ['https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv',
                'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv',
                'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
                ]

    nsn = zip(lista_url,listaaa)   #Uniendo las lista de urls con los nombres.
    nsn_listaa = (list(nsn))
    try:
        for x,n in nsn_listaa:         #Recorriendo las listas y aplicando la funcion fill()
            fill(x,n)
            logger.info('Creando archivo csv...')
        logger.info('Archivos csv creados correctamente!')
    except:
        logger.error('Algo salio mal al crear archivos csv')
 

def fecha_hora():
        time1 = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))
        time = time1.strftime('%d/%m/%Y | %H:%M')
        return time 

#Creando Data Frame para luego usar to_sql()
def df_to_sql():
    try:
        data_culturales_arg = datos_argentina()
        data_totales = datos_totales()
        data_cines = datos_cines()
        
        data_culturales_arg.to_sql(name='datos_argentina',con=engine,index=False,if_exists='append')
        data_totales.to_sql(name='datos_totales',con=engine,index=False,if_exists='append')
        data_cines.to_sql(name='datos_cines',con=engine,index=False,if_exists='append')
        logger.info('Datos agregados a la db correctamente!\n')
        logger.info('Proyecto terminado.')
    except:
        logger.critical('Hubo un problema al insertar los datos.')


if __name__ == '__main__':
    connect()
    create_schema()
    clean_csv()
    fill_csv()
    df_to_sql() 
    

