import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mtp
from sklearn.linear_model import LinearRegression

# Convertir de grados Celsius a Fahrenheit
def convertir_celsius_a_fahrenheit():
    # Read the CSV file
    datos = pd.read_csv("gradosCelsius_a_Fahrenheit.csv")
    datos.info()
    datos.head()

    sb.scatterplot(x="celsius", y="fahrenheit", data=datos)
    mtp.show()

    x = datos["celsius"]
    y = datos["fahrenheit"]
    print(x)
    print(y)

    x_procesada = x.values.reshape(-1, 1)
    print(x_procesada)
    y_procesada = y.values.reshape(-1,1)
    print(y_procesada)

    modelo = LinearRegression()
    modelo.fit(x_procesada, y_procesada)

    print("Temperatura en Fahrenheit: ", modelo.predict([[40]]))

# Convertir de grados Celsius a Kelvin
def convertir_celsius_a_kelvin():
    # Read the CSV file
    datos = pd.read_csv("gradosCelsius_a_Kelvin.csv")
    datos.info()
    datos.head()

    sb.scatterplot(x="celsius", y="kelvin", data=datos)
    mtp.show()

    x = datos["celsius"]
    y = datos["kelvin"]
    print(x)
    print(y)

    x_procesada = x.values.reshape(-1, 1)
    print(x_procesada)
    y_procesada = y.values.reshape(-1,1)
    print(y_procesada)

    modelo = LinearRegression()
    modelo.fit(x_procesada, y_procesada)

    print("Temperatura en Kelvin: ", modelo.predict([[40]]))

# Convertir de grados Celsius a Rankine
def convertir_celsius_a_rankine():
    # Read the CSV file
    datos = pd.read_csv("gradosCelsius_a_Rankine.csv")
    datos.info()
    datos.head()

    sb.scatterplot(x="celsius", y="rankine", data=datos)
    mtp.show()

    x = datos["celsius"]
    y = datos["rankine"]
    print(x)
    print(y)

    x_procesada = x.values.reshape(-1, 1)
    print(x_procesada)
    y_procesada = y.values.reshape(-1,1)
    print(y_procesada)

    modelo = LinearRegression()
    modelo.fit(x_procesada, y_procesada)

    print("Temperatura en Rankine: ", modelo.predict([[40]]))

# Main function para seleccionar la opción
def main():
    print("Seleccione una opción:")
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Celsius a Kelvin")
    print("3. Convertir de Celsius a Rankine")

    opcion = input("Ingrese el número de la opción seleccionada: ")

    if opcion == "1":
        convertir_celsius_a_fahrenheit()
    elif opcion == "2":
        convertir_celsius_a_kelvin()
    elif opcion == "3":
        convertir_celsius_a_rankine()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
