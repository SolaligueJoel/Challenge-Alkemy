from app import buscar_csv, fecha_hora
import pandas as pd


################### PROCESAMIENTO DE DATOS ###################
data_museo = buscar_csv('museo')
data_cine = buscar_csv('cine')
data_biblioteca = buscar_csv('biblioteca_popular')

def datos_culturales():
    df_museo_csv = pd.read_csv(data_museo,encoding='utf-8')
    df_cine = pd.read_csv(data_cine,encoding='utf-8')
    df_biblio = pd.read_csv(data_biblioteca)

    #Limpiando las columnas de los dataframe
    df_museo_csv.columns = [x.lower().replace('í','i').replace('ó','o').replace('Ã','i').replace('é','e').replace('ñ','n').replace('ã','o').replace('³','').replace('ao±o','anio').replace('TelÃ©fono','telefono').replace('o©','e').replace('categoro­a','categoria') for x in df_museo_csv.columns]
    df_cine.columns = [x.lower().replace('í','i').replace('ó','o').replace('Ã','i').replace('é','e').replace('ñ','n').replace('ã','o').replace('³','').replace('ao±o','anio').replace('TelÃ©fono','telefono').replace('o©','e').replace('categoro­a','categoria') for x in df_cine.columns]
    df_biblio.columns = [x.lower().replace('í','i').replace('ó','o').replace('Ã','i').replace('é','e').replace('ñ','n').replace('ã','o').replace('³','').replace('ao±o','anio').replace('TelÃ©fono','telefono').replace('o©','e').replace('categoro­a','categoria') for x in df_biblio.columns]
    

    return [df_museo_csv,df_cine,df_biblio]


############### Extrayendo datos de museo ###############
def datos_museo():
    df_museo_one = datos_culturales()
    df_museo = df_museo_one[0]

    df_museo.assign(categoria=pd.NA,id_departamento=pd.NA)

    #Limpiando las columnas del dataframe museo
    museo_a = df_museo.cod_loc.to_list()
    museo_b = df_museo.idprovincia.to_list()
    museo_c = df_museo.iddepartamento.to_list()
    museo_d = df_museo.categoria.to_list()
    museo_e = df_museo.provincia.to_list()
    museo_f = df_museo.localidad.to_list()
    museo_g = df_museo.nombre.to_list()
    museo_h = df_museo.direccion.to_list()
    museo_i = df_museo.cp.to_list()
    museo_j = df_museo.telefono.to_list()
    museo_k = df_museo.mail.to_list()
    museo_l = df_museo.web.to_list()

    return [museo_a, museo_b, museo_c,museo_d,museo_e,museo_f,museo_g,museo_h,museo_i,museo_j,museo_k,museo_l]



    ############### Extrayendo datos de cine ###############
def datos_cine():
    df_cine_one = datos_culturales()
    df_cine = df_cine_one[1]

    cine_a = df_cine.cod_loc.to_list()
    cine_b = df_cine.idprovincia.to_list()
    cine_c = df_cine.iddepartamento.to_list()
    cine_d = df_cine.categoria.to_list()
    cine_e = df_cine.provincia.to_list()
    cine_f = df_cine.localidad.to_list()
    cine_g = df_cine.nombre.to_list()
    cine_h = df_cine.direccion.to_list()
    cine_i = df_cine.cp.to_list()
    cine_j = df_cine.telefono.to_list()
    cine_k = df_cine.mail.to_list()
    cine_l = df_cine.web.to_list()

    return [cine_a,cine_b,cine_c,cine_d,cine_e,cine_f,cine_g,cine_h,cine_i,cine_j,cine_k,cine_l ]

    #Extrayendo datos de biblioteca
def datos_biblio():
    df_biblio_one = datos_culturales()
    df_biblio = df_biblio_one[2]
    new_df_biblio = df_biblio.assign(id_departamento='NaN',categoria='NaN')


    biblio_a = new_df_biblio.cod_loc.to_list()
    biblio_b = new_df_biblio.idprovincia.to_list()
    biblio_c = new_df_biblio.iddepartamento.to_list()
    biblio_d = new_df_biblio.categoria.to_list()
    biblio_e = new_df_biblio.provincia.to_list()
    biblio_f = new_df_biblio.localidad.to_list()
    biblio_g = new_df_biblio.nombre.to_list()
    biblio_h = new_df_biblio.domicilio.to_list()
    biblio_i = new_df_biblio.cp.to_list()
    biblio_j = new_df_biblio.telefono.to_list()
    biblio_k = new_df_biblio.mail.to_list()
    biblio_l = new_df_biblio.web.to_list()
    
    return [biblio_a,biblio_b,biblio_c,biblio_d,biblio_e,biblio_f,biblio_g,biblio_h,biblio_i,biblio_j,biblio_k,biblio_l]

    

########### UNIENDO LOS DATOS OBTENIDOS ###########
def datos_argentina():
    a,b,c = datos_museo(),datos_cine(),datos_biblio()
    
    lista_cod_localidad = a[0]+b[0]+c[0]
    lista_id_provincia = a[1]+b[1]+c[1]
    lista_id_departamento = a[2]+b[2]+c[2]
    lista_categoria = a[3]+b[3]+c[3]
    lista_provincia = a[4]+b[4]+c[4]
    lista_localidad = a[5]+b[5]+c[5]
    lista_nombre = a[6]+b[6]+c[6]
    lista_domicilio = a[7]+b[7]+c[7]
    lista_codigo_postal = a[8]+b[8]+c[8]
    lista_telefono = a[9]+b[9]+c[9]
    lista_mail = a[10]+b[10]+c[10]
    lista_web = a[11]+b[11]+c[11]



    #Creando diccionario para luego insertar en la base de datos, en tabala: datos_argentina
    datos_extraidos = {'cod_localidad':lista_cod_localidad,'id_provincia':lista_id_provincia,'id_departamento':lista_id_departamento,'categoria':lista_categoria,
                    'provincia':lista_provincia,'localidad':lista_localidad,'nombre':lista_nombre,'domicilio':lista_domicilio,'codigo_postal':lista_codigo_postal,
                    'numero_de_telefono':lista_telefono,'mail':lista_mail,'web':lista_web,'fecha_de_carga':fecha_hora()}
    
    data_frame = pd.DataFrame(datos_extraidos)

    return data_frame


def datos_totales():
    df_museo_one = datos_culturales()
    df_museo = df_museo_one[0]
    cantidad_datos_museo = len(df_museo)

    df_cine_one = datos_culturales()
    df_cine = df_cine_one[1]
    cantidad_datos_cine = len(df_cine)
    
    df_biblio_one = datos_culturales()
    df_biblio = df_biblio_one[2]
    cantidad_datos_biblio = len(df_biblio)

    
    datos_categoria = len(df_cine_one)
    suma_toal  = cantidad_datos_museo +  cantidad_datos_cine + cantidad_datos_biblio
    datos_provincia = datos_categoria * 2 

    #Creando diccionario para luego insertar en la base de datos, en tabla: datos_totales
    datos_categoria = {'registro_categoria':[datos_categoria],'registros_fuente':[suma_toal],'registros_prov_cat':[datos_provincia],'fecha_de_carga':fecha_hora()}

    datos_categoria_df = pd.DataFrame(datos_categoria)
    
    return datos_categoria_df
    
    
def datos_cines():
    df_cine_one = datos_culturales()
    df_cine_dos = df_cine_one[1]
    cantidad_de_pantallas = df_cine_dos.pantallas.to_list()
    
    provincias_cine = df_cine_dos.provincia.to_list()
    
    #Creando diccionario para luego insertar en la base de datos, en tabla: datos_cines
    espacios_incaa = df_cine_dos.espacio_incaa.to_list()
    
    datos_cines = {'provincia':provincias_cine,'cantidad_pantallas':cantidad_de_pantallas,'cantidad_espacios_incaa':espacios_incaa,'fecha_de_carga':fecha_hora()}
    datos_cines_df = pd.DataFrame(datos_cines)
    
    return datos_cines_df


