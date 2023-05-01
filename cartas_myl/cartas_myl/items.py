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
