import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Cargar los datos
df = pd.read_csv('global_food_prices.csv', low_memory=False)

# Filter the dataframe for the exchange rate
df_exchange_rate = df[df['cm_name'] == 'Exchange rate - Retail']

# Print the unique values in the 'um_id' column for the filtered dataframe
print(df_exchange_rate['um_id'].unique())

# Identificar los productos alimenticios más caros y más baratos en promedio
precios_promedio = df.groupby('cm_name')['mp_price'].mean().sort_values()
producto_mas_barato = precios_promedio.idxmin()
producto_mas_caro = precios_promedio.idxmax()

print(f'El producto más barato en promedio es: {producto_mas_barato}')
print(f'El producto más caro en promedio es: {producto_mas_caro}')

# Analizar la relación entre el tipo de moneda y los precios de los alimentos
precios_moneda = df.groupby('cur_name')['mp_price'].mean().sort_values()

# Graficar el precio promedio para cada moneda
fig = px.bar(x=precios_moneda.index, y=precios_moneda.values, labels={'x': 'Moneda', 'y': 'Precio promedio'})
fig.update_layout(title='Precio promedio para cada moneda')
pio.write_html(fig, file='precios_moneda.html', auto_open=False)

precios_promedio_por_año = df.groupby('mp_year')['mp_price'].mean()

fig = px.line(x=precios_promedio_por_año.index, y=precios_promedio_por_año.values, labels={'x': 'Año', 'y': 'Precio promedio'})
fig.update_layout(title='Precio promedio por año')
pio.write_html(fig, file='precios_promedio_por_año.html', auto_open=False)

precios_producto_año = df.groupby(['cm_name', 'mp_year'])['mp_price'].mean().reset_index()
precios_producto_año_pivot = precios_producto_año.pivot_table(index='cm_name', columns='mp_year', values='mp_price')

fig = px.imshow(precios_producto_año_pivot, labels=dict(x='Año', y='Producto', color='Precio promedio'))
fig.update_layout(title='Precio promedio para cada producto y año')
pio.write_html(fig, file='precios_producto_año.html', auto_open=False)

# Filtrar datos para un rango de años específico (opcional)
df = df[(df['mp_year'] >= 2010) & (df['mp_year'] <= 2020)]

# Obtener la lista de regiones únicas
regiones = df['adm0_name'].unique()

# Establecer el número de regiones por gráfico
regiones_por_grafico = 40

# Calcular el número de gráficos necesarios
num_graficos = len(regiones) // regiones_por_grafico + (len(regiones) % regiones_por_grafico > 0)

# Crear gráficos de líneas separados para cada subconjunto de regiones
for i in range(num_graficos):
    inicio = i * regiones_por_grafico
    fin = inicio + regiones_por_grafico
    subconjunto_regiones = regiones[inicio:fin]

    # Filtrar datos para el subconjunto de regiones
    datos_subconjunto = df[df['adm0_name'].isin(subconjunto_regiones)]

    # Calcular el precio promedio por año y región
    precios_año_region = datos_subconjunto.groupby(['mp_year', 'adm0_name'])['mp_price'].mean().reset_index()

    # Graficar el precio promedio por año y región
    fig = px.line(precios_año_region, x='mp_year', y='mp_price', color='adm0_name', labels={'mp_year': 'Año', 'mp_price': 'Precio promedio', 'adm0_name': 'Región'})
    fig.update_layout(title=f'Precio promedio de productos alimenticios por año y región (Regiones {inicio + 1} a {fin})')
    pio.write_html(fig, file=f'precios_region_{i + 1}.html', auto_open=False)