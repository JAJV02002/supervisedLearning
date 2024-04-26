import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mtp
from sklearn.linear_model import LinearRegression

# Read the CSV file
datos = pd.read_csv("grados.csv")
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
