# SisTradingAuto

Sistema automatizado para trading.

## Descripción

SisTradingAuto es una aplicación en Python diseñada para automatizar el análisis técnico de criptomonedas. Descarga datos históricos, calcula indicadores técnicos clave y genera señales de compra/venta basadas en estrategias de cruce de medias móviles.

**⚠️ Disclaimer:** Este proyecto es solo para fines educativos. No constituye asesoramiento financiero.

## Características 

- Descargar datos históricos de criptomonedas desde Yahoo Finance (`yfinance`).
- Calcular indicadores técnicos:
  - Media Móvil Simple (SMA) de 7 y 20 días
  - Volatilidad basada en desviación estándar
  - Cambio porcentual diario
- Generar señales de compra/venta basadas en cruces de medias móviles
- Visualizar gráficos:
  - Precio de cierre y medias móviles
  - Volatilidad
  - Cambio porcentual diario
- Guardar los datos analizados en un archivo CSV

## Instalación

```bash
git clone https://github.com/tuusuario/SisTradingAuto.git
cd SisTradingAuto
pip install yfinance matplotlib pandas

```

## Uso

SisTradingAuto está en desarrollo, por lo que algunas funcionalidades pueden cambiar. Aquí tienes un ejemplo básico de uso:

1. **Instala las dependencias** siguiendo las instrucciones de instalación:
    ```bash
    git clone https://github.com/tuusuario/SisTradingAuto.git
    cd SisTradingAuto
    pip install yfinance matplotlib pandas
    ```
2. **Ejecuta el script principal** para descargar y analizar los datos.
3. **Configura los parámetros de trading** (símbolo de la criptomoneda, fechas, etc.) en el archivo de configuración o directamente en el código.
4. **Revisa los resultados** generados en los archivos CSV y los gráficos en la carpeta de salida.

> **Nota:** Consulta la documentación y los comentarios en el código para más detalles sobre la configuración y personalización de estrategias.


## Contribución

¡Las contribuciones son bienvenidas! Si deseas colaborar, puedes abrir un issue para reportar errores o sugerir mejoras, o enviar un pull request con tus cambios. Este es mi primer proyecto en Python, por lo que cualquier ayuda, consejo o revisión será muy apreciada.

## Licencia

Este proyecto se distribuye bajo la licencia MIT, lo que permite su uso, modificación y distribución libremente, siempre que se incluya el aviso de copyright y la licencia original. Consulta el archivo `LICENSE` para más detalles.

Copyright (c) 2025 Santiago Pérez Guerrero

