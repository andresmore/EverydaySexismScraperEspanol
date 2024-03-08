# Scraper - Everyday sexism en español

Este proyecto permite realizar el scraping de la página [Everyday sexism](https://everydaysexism.com/) para obtener los testimonios de relatos de sexismo en la vida cotidiana narrados por mujeres de los paises que hablan Español, disponibles en el sitio web: [Argentina](https://everydaysexism.com/country/ar/), [España](https://everydaysexism.com/country/es/) y [México](https://everydaysexism.com/country/mx/).

Mi objetivo al crear este scraper es proveer un conjunto de datos fácilmente procesables por cualquier persona interesada en el tema, para que puedan realizar análisis de texto, minería de datos, visualizaciones, etc. y así poder construir herramientas que ayuden a visibilizar y entender este fenómeno.  

Todos los créditos de los testimonios obtenidos con este scraper deben ser atribuidos a la página [Everyday sexism](https://everydaysexism.com/), ya que el objetivo de este proyecto es únicamente facilitar el acceso a los datos.

## Uso del scraper

El scraper está escrito en Python y utiliza la librería [Scrapy](https://scrapy.org/). Para ejecutarlo, primero debes instalar Scrapy. Puedes hacerlo con el siguiente comando:

```bash
pip install scrapy
```

Una vez instalado Scrapy, puede ejecutar el scraper con el siguiente comando:

```bash
cd ed_sexism
scrapy crawl sexism -o sexism.json
```
    