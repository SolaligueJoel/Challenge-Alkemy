DROP TABLE IF EXISTS datos_argentina;

CREATE TABLE datosArgentina(
    [cod_localidad] INTEGER PRIMARY KEY AUTOINCREMENT,
    [id_provincia] = INT NOT NULL,
    [id_departamento = INT,
    [categoria] = TEXT,
    [provincia] = VARCHAR,
    [localidad] = VARCHAR,
    [nombre] = VARCHAR,
    [domicilio] = VARCHAR,
    [codigo_postal] = INTEGER,
    [numero_de_telefono] = INTEGER,
    [mail] = TEXT,
    [web] = TEXT,
    [fecha] = TIMESTAMP WITHOUT TIME ZONE NOT NULL
);


DROP TABLE IF EXISTS datos_totales;

CREATE TABLE datos_totales(
    [registros_categoria] INT,
    [registros_fuente] INT,
    [registros_prov_cat] INT,
    [fecha] tIMESTAMP WITHOUT TIME ZONE NOT NULL
);

DROP TABLE IF EXISTS datos_cines;

CREATE TABLE datos_cines(
    [provincia] VARCHAR,
    [cantidad_pantallas] INT,
    [cantidad_espacios_incaa] INT,
    [fecha] tIMESTAMP WITHOUT TIME ZONE NOT NULL
);




