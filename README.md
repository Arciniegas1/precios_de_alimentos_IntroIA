# precios_de_alimentos_IntroIA
Objetivo General
El objetivo principal de este análisis de datos es investigar y comprender las tendencias y patrones en
un conjunto de datos que contiene información sobre los precios de productos alimentarios en diferentes
mercados y regiones. Mediante este análisis, buscamos extraer información valiosa que pueda respaldar la 
toma de decisiones relacionadas con la economía y la producción de alimentos.

Objetivos Específicos
Identificar los productos alimentarios más caros y más baratos en promedio a lo largo de los años y 
regiones. Esto nos ayudará a comprender las fluctuaciones de precios y su impacto en la accesibilidad a 
los alimentos en diferentes áreas geográficas.

Analizar la relación entre el tipo de moneda y los precios de los productos alimentarios. Investigaremos 
si hay una correlación entre la moneda utilizada y los precios de los alimentos, lo que podría tener 
implicaciones en términos de estabilidad económica.

Datos Utilizados
Los datos utilizados en este análisis provienen del archivo CSV "global_food_prices.csv". El conjunto 
de datos contiene múltiples columnas que proporcionan información detallada sobre los productos 
alimentarios, los mercados, las fechas y los precios. A continuación, se describe brevemente cada 
variable:

adm0_id: Identificación del país.
adm0_name: Nombre del país.
adm1_id: Identificación de la subdivisión administrativa.
adm1_name: Nombre de la subdivisión administrativa.
mkt_id: Identificación del mercado.
mkt_name: Nombre del mercado.
cm_id: Identificación del producto.
cm_name: Nombre del producto.
cur_id: Identificación de la moneda.
cur_name: Nombre de la moneda.
pt_id: Identificación del tipo de precio.
pt_name: Nombre del tipo de precio.
um_id: Identificación de la unidad de medida.
um_name: Nombre de la unidad de medida.
mp_month: Mes del precio.
mp_year: Año del precio.
mp_price: Precio del producto en la unidad de medida especificada.
mp_commoditysource: Fuente de datos del producto.
Análisis Realizado
En el cuaderno (notebook) adjunto, hemos realizado el siguiente análisis de datos:

Exploración Inicial de los Datos: Hemos cargado el conjunto de datos y realizado una exploración 
inicial para comprender la estructura y el contenido de los datos.

Limpieza de Datos: Hemos identificado y manejado datos faltantes, duplicados y posibles errores 
en las columnas.

Análisis de Precios Promedio: Hemos calculado y visualizado los precios promedio de los productos 
alimentarios a lo largo de los años y las regiones. Esto incluye la identificación de los productos 
más caros y más baratos.

Análisis de la Relación entre Moneda y Precios: Hemos investigado si existe una correlación entre 
la moneda utilizada y los precios de los alimentos.

Visualizaciones: Hemos utilizado gráficos, como histogramas y gráficos de barras, para representar 
visualmente los resultados del análisis.

Variables Relevantes
Las variables que se consideran inicialmente relevantes para cumplir con los objetivos del análisis 
son mp_month, mp_year, mp_price, cm_name, cur_name, adm0_name, y adm1_name. Sin embargo, a medida 
que avanzamos en el análisis, podríamos decidir eliminar o agregar variables según sea necesario 
para responder a preguntas específicas.
