# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 4: Educación de calidad ''')
# Insertamos texto con formato
st.markdown("""Recursos para el Fortalecimiento Educativo en India.""")
# Insertamos una imagen
st.image("Goal-04.png")

# Usaremos un deslizador
#st.sidebar.header("Presupuesto")
# Definimos los parámetros de nuestro deslizador:
  # Límite inferior: 20000000000
  # Límite superior: 64000000000
  # Valor inicial: 40000000000
presupuesto = st.sidebar.slider("Presupuesto", 500, 2500, 1000)

#st.sidebar.header("Porcentaje de Becas")
#porcentaje_becas = st.sidebar.slider("Porcentaje de Becas", 0.0, 1.0, 0.2)

# Cargamos el archivo con los datos (.csv)
datos =  pd.read_csv('ODS4.csv', encoding='latin-1')
# Seleccionamos las variables
X = pd.DataFrame(datos, columns=['Inversion'])
y = datos['Termino']

# Creamos y entrenamos el modelo
from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X,y)
score = LR.score(X, y)
st.write("El ajuste es de: \n", score)

# Extraemos los coeficientes de la regresión
b1 = LR.coef_
b0 = LR.intercept_

indice = b0 + b1*presupuesto
st.write("El índice de término es de: \n", indice)
#st.write(f'El porcentaje de término es: {impacto:.2f}%')
