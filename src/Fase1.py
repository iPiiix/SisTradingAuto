"""
FASE 1 - Sistemas Automatizado de Tradings
Autor: Santiago Pérez Guerrero
Descripcion: Script para obten
er y analizar datos finacieros
"""
# Importar librerias
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def obtener_datos_cripto(simbolo='BTC-USD', periodo='1mo'):
    """Función para descargar datos históricos de una criptomoneda"""
    try:  
        print(f"Descargando datos de {simbolo}...")  
        datos = yf.download(simbolo, period=periodo, interval='1d')
        
        if datos.empty:
            print("No se encontraron datos para el símbolo especificado.")
            return None
        
        if isinstance(datos.columns, pd.MultiIndex):
            datos.columns = datos.columns.get_level_values(0)

        print(f"Datos descargados desde {datos.index[0].date()} hasta {datos.index[-1].date()}")
        return datos
    except Exception as e:
        print(f"Error al descargar datos: {e}")
        return None
    
def mostrar_resumen(df):
    """Muestra un resumen de los datos obtenidos."""
    print("\n" + "="*50)
    print("RESUMEN DE DATOS")
    print("="*50)
    print(f"\nPrecio actual: ${df['Close'].iloc[-1]:.2f}")
    print(f"Precio máximo: ${df['High'].max():.2f}")
    print(f"Precio mínimo: ${df['Low'].min():.2f}")
    print(f"Volumen promedio: {df['Volume'].mean():,.0f}")
    print("\nÚltimos 5 días:")
    print(df[['Open', 'High', 'Low', 'Close', 'Volume']].tail())

def calcular_indicadores(df):
    """Calcula indicadores técnicos simples."""
    print("\nCalculando indicadores técnicos...")

    # Media Móvil Simple (SMA) y Volatilidad (7 y 20 días)
    df['SMA_7'] = df['Close'].rolling(window=7).mean()
    df['SMA_20'] = df['Close'].rolling(window=20).mean() 

    # Volatilidad (desviación estándar de los precios de cierre en una ventana móvil de 20 días)
    df['Volatilidad'] = df['Close'].rolling(window=20).std()

    # Cambio porcentual diario
    df['Cambio_Porc'] = df['Close'].pct_change() * 100

    print("Indicadores calculados.")
    return df

def generar_señales(df):
    """Genera señales de compra/venta basadas en cruces de medias móviles y muestra resumen."""
    # Inicializar señal
    df['Señal'] = 0
    df.loc[df['SMA_7'] > df['SMA_20'], 'Señal'] = 1  # Compra
    df.loc[df['SMA_7'] < df['SMA_20'], 'Señal'] = -1 # Venta

    # Detectar cruces
    df['Cruce'] = df['Señal'].diff()

    # Contar cruces
    cruces_compra = df[df['Cruce'] == 2].shape[0]   # -1 → 1
    cruces_venta = df[df['Cruce'] == -2].shape[0]   # 1 → -1

    print(f"\nTotal señales de compra: {cruces_compra}")
    print(f"Total señales de venta: {cruces_venta}")

    return df

def backtesting(df, capital_inicial=1000):
    """Realiza un backtesting simple basado en las señales generadas."""
    capital = capital_inicial
    posiciones = 0  # Número de unidades compradas
    operaciones = [] # Historial de operaciones

    for i in range(1, len(df)):
        if df['Cruce'].iloc[i] == 2:  # Señal de compra
            if capital >= df['Close'].iloc[i]:
                unidades = capital // df['Close'].iloc[i]
                posiciones += unidades
                capital -= unidades * df['Close'].iloc[i]
                print(f"Compra: {unidades} unidades a ${df['Close'].iloc[i]:.2f} el {df.index[i].date()}")

        elif df['Cruce'].iloc[i] == -2:  # Señal de venta
            if posiciones > 0:
                capital += posiciones * df['Close'].iloc[i]
                print(f"Venta: {posiciones} unidades a ${df['Close'].iloc[i]:.2f} el {df.index[i].date()}")
                posiciones = 0

    # Valor final
    valor_final = capital + posiciones * df['Close'].iloc[-1]
    ganancia_perdida = valor_final - capital_inicial
    print(f"\nValor final de la cartera: ${valor_final:.2f}")
    print(f"Ganancia/Pérdida total: ${ganancia_perdida:.2f}")

    return valor_final

def graficar_datos(df, simbolo):
    """Genera gráficos de los datos y los indicadores."""
    print("\nGenerando gráficos...")

    plt.figure(figsize=(14, 10))

    # Gráfico de precios y medias móviles
    plt.subplot(3, 1, 1)
    plt.plot(df['Close'], label='Precio de Cierre', color='blue')
    plt.plot(df['SMA_7'], label='SMA 7 días', color='orange')
    plt.plot(df['SMA_20'], label='SMA 20 días', color='green')
    plt.title(f'{simbolo} - Precio y Medias Móviles')
    plt.xlabel('Fecha')
    plt.ylabel('Precio (USD)')
    plt.legend()
    plt.grid()

    # Gráfico de Volatilidad
    plt.subplot(3, 1, 2)
    plt.plot(df['Volatilidad'], label='Volatilidad (20 días)', color='red')
    plt.title(f'{simbolo} - Volatilidad')
    plt.xlabel('Fecha')
    plt.ylabel('Volatilidad')
    plt.legend()
    plt.grid()

    # Gráfico de Cambio Porcentual Diario
    plt.subplot(3, 1, 3)
    plt.plot(df['Cambio_Porc'], label='Cambio Porcentual Diario', color='purple')
    plt.title(f'{simbolo} - Cambio Porcentual Diario')
    plt.xlabel('Fecha')
    plt.ylabel('Cambio (%)')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()
    print("Gráficos generados.")

def main():
    """Función principal para ejecutar el análisis."""
    print("\n" + "="*50)
    print("SISTEMA DE TRADING AUTOMATIZADO")
    print("="*50)

    #Configuración
    SIMBOLO = 'BTC-USD'  # Criptomoneda a analizar
    PERIODO = '3mo'     # Período de datos a descargar

    #Ejecutar pipeline
    datos = obtener_datos_cripto(SIMBOLO, PERIODO)

    if datos is not None and not datos.empty:
        mostrar_resumen(datos)
        datos = calcular_indicadores(datos)
        datos = generar_señales(datos)

        print("\n" + "="*50)
        print("INICIO BACKTESTING")
        print("="*50)
        backtesting(datos, capital_inicial=1000)

        graficar_datos(datos, SIMBOLO)

        datos.to_csv(f"{SIMBOLO.replace('-','_')}_analisis.csv")
        print("\n Datos guardados en '{nombre_archivo}'")
    else:
        print("No se pudieron obtener datos para el análisis.")
if __name__ == "__main__":
    main()
