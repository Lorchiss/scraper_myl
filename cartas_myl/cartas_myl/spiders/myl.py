import scrapy
from cartas_myl.items import Carta

class MylSpider(scrapy.Spider):
    name = "myl"
    allowed_domains = ["myl.fandom.com"]
    start_urls = ['https://myl.fandom.com/es/wiki/Nueva_Era',
                  'https://myl.fandom.com/es/wiki/Lista_de_cartas_de_Dominio',
                  'https://myl.fandom.com/es/wiki/Lista_de_cartas_de_Apocalipsis',
                  'https://myl.fandom.com/es/wiki/Furia']

    def parse(self,response):
        #print(response.xpath('//title/text()').get())
        links_cartas = response.xpath('//tr/td/a/@href')

        for link in links_cartas:
            yield response.follow(link, self.parse_ediciones)

    def parse_ediciones(self, response):
        #print(response.xpath('//title/text()').get())
        links = response.xpath('//dl/dd/i/a/@href')

        for link in links:
            yield response.follow(link, self.parse_listado)
                      
    def parse_listado(self,response):
        #print(response.xpath('//title/text()').get())
        links_cartas = response.xpath('//div[@class="mw-parser-output"]/table/tbody/tr/td[2]/a/@href')
        
        for i,link in enumerate(links_cartas):
            yield response.follow(link, self.parse_carta)


    def parse_carta(self, response):
        #print(response.xpath('//title/text()').get())
        carta = Carta()

        habilidad_completa = response.xpath('//table[@class="table_black"][2]//tr[2]/td/b/text() | //table[@class="table_black"][2]//tr[2]/td/text()').getall()
        habilidad_completa = ''.join(habilidad_completa).strip()
        
        tipo = response.xpath('//tr[th/b/text() = "Tipo"]/th[2]/text()').get()
        edicion =  response.xpath('//tr[th/b/text() = "Edición"]/th[2]/text()').get()

        if tipo is None or tipo == '\n':
            tipo = response.xpath('//tr[th/b/text() = "Tipo"]/th[2]/a/text()').get(default='').strip()
        else:
            tipo = tipo.strip()
            
        if tipo == "Aliado":
            raza = response.xpath('//tr[th/b/text() = "Raza"]/th[2]/text()').get()
            if raza is None or raza == '\n':
                raza = response.xpath('//tr[th/b/text() = "Raza"]/th[2]/a/text()').get().strip()
                if raza is None:
                    raza = 'Sin Raza'
            else:
                raza = raza.strip()
        else:
            raza = ""

        if edicion is None or edicion == '\n':
            edicion =  response.xpath('//tr[th/b/text() = "Edición"]/th[2]/a/text()').get(default='').strip()
        else:
            edicion = edicion.strip()


        carta['nombre']     = response.xpath('//div[@class="mw-parser-output"]/table/tbody/tr/td/b/text()').get()
        carta['tipo']       = tipo
        carta['fuerza']     = response.xpath('//tr[th/b/text() = "Fuerza"]/th[2]/text()').get(default='').strip()
        carta['coste']      = response.xpath('//tr[th/b/text() = "Coste de oro"]/th[2]/text()').get(default='').strip()
        carta['raza']       = raza
        carta['frecuencia'] = response.xpath('//tr[th/b/text() = "Frecuencia"]/th[2]/text()').get().strip()
        carta['edicion']    = edicion
        carta['habilidad']  = habilidad_completa

        yield carta