import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset_percepcion.csv")
print("OKEY! Archivo cargado correctamente")

#1 Cantidad de filas y columnas
filas, columnas = df.shape
print(f"La tabla contiene {filas} filas y {columnas} columnas.")

#2 Filtar por coincidencia
filtro_avanzado = df ["REGION"] == 3
df_filtrado = df[filtro_avanzado]

#3 Filtrar pot texto parcial
filtro_avanzado = df["REGION"].astype(str).str.startswith("1",na=False)
df_filtrado = df[filtro_avanzado]

print("----- Reporte Automatizado -----")

#4 Selección de Columnas Clave
print(df_filtrado[["REGION", "PONDERA"]].head())

#5 Agrupación y resumen
resumen = ( 
    df.groupby("REGION")["PONDERA"]
    .sum()
    .sort_values(ascending=False)
)
print("Resumen por región:")
print(resumen)

#6 Estructura de Control Automatizada
if (total := df_filtrado["PONDERA"].sum()) > 10000:
    print("Total: {total}")
else:
    print("Estado normal. Total: {total}")

#7 Gráfico de Barras Comparativo
print("\n[Generando GRAFICO de Barras]")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(
    data=df,
    x="REGION",
    y="PONDERA",
    estimator=sum,
    errorbar=None,
    palette="viridis",
)
plt.title("Suma de pondera por región", fontsize=14)
plt.xticks(rotation=20)

plt.savefig("grafico_barra.png", dpi=300)
plt.close()

#8 Gráfico de Torta Puro
top = resumen.nlargest(5)

plt.figure(figsize=(7,7))
plt.pie(
    top,
    labels=top.index,
    autopct="%1.1f%%",
    wedgeprops={"edgecolor": "white"}
)
plt.title("Distribución de pondera por región")
plt.savefig("grafico_torta.png", dpi=300)
plt.close()

print("\n¡Hecho! Los gráficos se guardaron correctamente en tu carpeta")

plt.tight_layout()
plt.show()


