"""
FASE 1 - Sistemas Automatizado de Tradings
Autor: Santiago Pérez Guerrero
Descripcion: Script para obtener y analizar datos finacieros
"""
# Importar librerias
import yfinance as yf

def obtener_datos_cripto(simbolo='BTC-USD', periodo='1mo'):
    print (f"Decargado datos de {simbolo}...")
    datos = yf.download(simbolo, period=periodo, interval='1d')
    print (f"Datos descargados desde {datos.index[0].date()} hasta {datos.index[-1].date()}")
    return datos

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

def generar_señales_simples(df):
    """Genera señales de compra/venta basadas en cruces de medias móviles."""
    df['Señal'] = 0
    df.loc[df['SMA_7'] > df['SMA_20'], 'Señal'] = 1  # Señal de compra
    df.loc[df['SMA_7'] < df['SMA_20'], 'Señal'] = -1 # Señal de venta

    # Detectar cruces
    df['Cruce'] = df['Señal'].diff()

    return df