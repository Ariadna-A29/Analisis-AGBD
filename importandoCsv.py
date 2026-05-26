import pandas as pd

#Solo ponemos el nombre exacto del archivo entre comillas
df=pd.read_csv("dataset_percepcion.csv")

print("OKEY! Archivo cargado correctamente")

#Mostrando las primeras filas del dataframe
print(df.head())

#Mostrar resultado que año sea igual a 2022
#resultado = df[df['ANIO'] == 2022]

#print(resultado)

total_visita = df['VISITA_ARTE'].count()
print(f"Total de registros: {total_visita}")

total_InteresE = df['INTERES_ECONOMIA'].sum()
print(f"Total de intereses Economia: {total_InteresE}")
