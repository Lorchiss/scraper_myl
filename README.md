# SCRAPER MYL

_La idea es hacer una API para hacer cosas interesantes con este juego de cartas. Inicialmente con el scraper obtendriamos una buena cantidad de cartas de Mitos y Leyendas ya que no hay un API a la cual consultar._

_Si estoy cometiendo alguna irregularidad porfavor notificarmelo._

### Pre-requisitos 📋

python

crear virtualenv

### Instalación 🔧

```
pip install scrapy
```
## Ejecutando Scraper ⚙️

```
scrapy crawl myl -o datos.json
```
Esto ejecuta el spider myl y retorna un archivo json con los datos solicitados.

## Estructura de las cartas

Las cartas están estructuradas de la siguiente manera:

- Nombre: el nombre de la carta, extraído de la página web.
- Tipo: el tipo de la carta, que puede ser común, rara, épica o legendaria.
- Fuerza: la fuerza de la carta, extraída de la página web.
- Coste: el coste de oro de la carta, extraído de la página web.
- Raza: la raza a la que pertenece la carta, que puede ser una de las siguientes: Sombra, Caballero, Defensor, Asesino, etc.
- Frecuencia: la frecuencia con la que aparece la carta, que puede ser una de las siguientes: Real, Cortesano, Vasallo, Sin Frecuencia, Oro, Promocional, Ultra Real, Real SP, Mega Real, Premium Foil, Legendaria, Milenaria.
- Edición: la edición en la que fue lanzada la carta.
- Habilidad: la habilidad completa de la carta, extraída de la página web.

Puedes ver el código fuente del scraper para obtener más detalles sobre cómo se extraen estas propiedades de la página web.


