import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cepeda Darrell NC = 0030    Fecha 5/11/2026

# crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de Lenguajes con 4 elementos por lista
pyt = ['Python', 1991, True, 1]
jva = ['Java', 1995, True, 3]
js = ['JavaScript', 1995, False, 2]
cpp = ['C++', 1985, True, 4]
php = ['PHP', 1995, False, 8]

# Creamos una lista de listas (conformando la tabla)
lista_lenguajes = [pyt, jva, js, cpp, php]
# print(lista_lenguajes)

# Utilizar pandas para organizar la tabla (DataFrame o marco de datos)
# A cada columna le ponemos un nombre
df_lenguajes = pd.DataFrame(
    lista_lenguajes,
    columns=["Nombre", "Año", "Tipado_Fuerte", "Popularidad"]
)

print(df_lenguajes)

# creamos el archivo CSV y lo guardamos en CSV
df_lenguajes.to_csv("lenguajes.csv", index=False)

# crear grafica de lineas
# donde X es Nombre en el eje horizontal
# donde Y es Popularidad en el eje vertical
plt.plot(df_lenguajes["Nombre"], df_lenguajes["Popularidad"])
plt.title("Graficas Lenguajes 0030")
plt.xlabel("Nombre de los lenguajes")
plt.ylabel("Popularidad ranking")
plt.show()

# creamos una grafica de puntos
plt.scatter(df_lenguajes["Nombre"], df_lenguajes["Popularidad"])
plt.show()

# Grafica de barras
plt.bar(df_lenguajes["Nombre"], df_lenguajes["Popularidad"])

# Agregar título y etiquetas a los ejes
plt.title("Lenguajes 0030")
plt.xlabel("Los lenguajes")
plt.ylabel("Popularidad ranking")

# Mostrar la gráfica
plt.show()

# Ordenar grafica de barras de manera descendente
# De la mas grande a la mas pequeña
df_l_ordenar = df_lenguajes.sort_values("Popularidad", ascending=False)

plt.bar(df_lenguajes["Nombre"], df_l_ordenar["Popularidad"])
plt.show()

# coloreando la grafica
df_l_ordenar = df_lenguajes.sort_values("Popularidad", ascending=False)

plt.bar(
    df_lenguajes["Nombre"],
    df_l_ordenar["Popularidad"],
    color=["b", "g", "c", "m", "y"]
)

plt.show()

# Grafica de pastel
plt.plot(df_lenguajes["Nombre"], df_lenguajes["Popularidad"])
plt.pie(
    df_lenguajes["Popularidad"],
    labels=df_lenguajes["Nombre"]
)
plt.show()

print("Programa ejecutado por Cepeda Darrell NC = 0030")