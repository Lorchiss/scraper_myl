# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Carta(scrapy.Item):
    nombre    = scrapy.Field() 
    tipo      = scrapy.Field()
    fuerza    = scrapy.Field()
    coste     = scrapy.Field()
    raza      = scrapy.Field()
    frecuencia= scrapy.Field()
    edicion   = scrapy.Field()
    habilidad = scrapy.Field()
