import scrapy
from scraper_tor.items import Carta

class TorSpider(scrapy.Spider):
    name = "tor"
    allowed_domains = ["myl.fandom.com"]
    start_urls = ['https://myl.fandom.com/es/wiki/Nueva_Era']

    custom_settings = {
        'DEPTH_LIMIT': 0,
        # otros ajustes personalizados aquí si los tienes
    }


    def parse(self,response):
        print(response.xpath('//title/text()').get())
        links_cartas = response.xpath('//tr/td/a/@href').extract()
        for link in links_cartas:
            yield response.follow(link,self.parse_listado)
    
    def parse_listado(self,response):
        links_cartas = response.xpath('//div[@class="mw-parser-output"]/table/tbody/tr/td[2]/a/@href').extract()
        links_cartas.pop(0)
        for link in links_cartas:
            yield response.follow(link, self.parse_carta)


    def parse_carta(self, response):
        carta = Carta()

        habilidad_completa = response.xpath('//table[@class="table_black"][2]//tr[2]/td/b/text() | //table[@class="table_black"][2]//tr[2]/td/text()').extract()
        habilidad_completa = ''.join(habilidad_completa).strip()
        
        raza = response.xpath('//tr[th/b/text() = "Raza"]/th[2]/text()').get().strip()
        if raza == '':
            raza = response.xpath('//tr[th/b/text() = "Raza"]/th[2]/a/text()').get().strip()

        edicion =  response.xpath('//tr[th/b/text() = "Edición"]/th[2]/text()').get().strip()
        if edicion == '':
            edicion =  response.xpath('//tr[th/b/text() = "Edición"]/th[2]/a/text()').get()

        tipo = response.xpath('//tr[th/b/text() = "Tipo"]/th[2]/text()').get().strip()
        if tipo == '':
            tipo = response.xpath('//tr[th/b/text() = "Tipo"]/th[2]/a/text()').get().strip()

        
        carta['nombre']     = response.xpath('//div[@class="mw-parser-output"]/table/tbody/tr/td/b/text()').get()
        carta['tipo']       = tipo
        carta['fuerza']     = response.xpath('//tr[th/b/text() = "Fuerza"]/th[2]/text()').get().strip()
        carta['coste']      = response.xpath('//tr[th/b/text() = "Coste de oro"]/th[2]/text()').get().strip()
        carta['raza']       = raza
        carta['frecuencia'] = response.xpath('//tr[th/b/text() = "Frecuencia"]/th[2]/text()').get().strip()
        carta['edicion']    = edicion
        carta['habilidad']  = habilidad_completa

        yield carta