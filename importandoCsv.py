#Importamos las librerías necesarias
import pandas as pd
import matplotlib as plt
import seaborn as sns

#Cargo de datos
#Solo ponemos el nombre exacto del archivo entre comillas
df = pd.read_csv("dataset_percepcion.csv")

print("OKEY! Archivo cargado correctamente")

#Logica de filtrado
filtro_avanzado = df["DESTAQUE_SALUD"].str.starswith("1", na= False)
df_filtrado = df(filtro_avanzado)
suma_dinero = df_filtrado["INFORMACION_MEDICINA_SALUD"].sum()

print("----- Reporte Automatizado -----")
print(f"Monto finalizado: {suma_dinero:.2f} puntos")

#Condicional
if default_limite_alto := (suma_dinero > 500):
    print("Alerta! La información supera el limite.")
    print("Requiere revisión inmediata")
elif suma_dinero < 100:
    print("Aviso: mercado moderado/alto")
    print("Monitorear comportamiento prox trim")
else:
    print("Mercado estable, sin alertas por el momento.")

#-------------------------------------
#Gráfico de barras usando toda DF
#-------------------------------------
print("\n[Generando GRAFICO de Barras]")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(
    data=df,
    x="DESTAQUE_SALUD",
    y="INFORMACION_MEDICINA_SALUD",
    estimator=sum,
    errorbar=None,
    palette="viridis",
)
plt.title("Comparativa de información medicina por región", fontsize=14)
plt.xticks(rotation=20)

plt.savefig("grafico_barra.png", dpi=300)
plt.close()

print("\n¡Hecho! Los gráficos se guardaron correctamente en tu carpeta")

plt.tight_layout()
plt.show()


