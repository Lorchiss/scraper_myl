from functools import singledispatch

class Carta:
    def __init__(self, nombre, habilidad):
        self.nombre = nombre
        self.habilidad = habilidad
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
class Oro(Carta):
    def __init__(self, nombre, habilidad):
        super().__init__(nombre, habilidad)

class Aliado(Carta):
    def __init__(self, nombre, habilidad, fuerza):
        super().__init__(nombre, habilidad)
        self.fuerza = fuerza

class ATT(Carta):
    def __init__(self, nombre, habilidad, coste):
        super().__init__(nombre, habilidad)
        self.coste = coste

class Arma(ATT):
    def __init__(self, nombre, habilidad, coste):
        super().__init__(nombre, habilidad, coste)

class Totem(ATT):
    def __init__(self, nombre, habilidad, coste):
        super().__init__(nombre, habilidad, coste)

class Talisman(ATT):
    def __init__(self, nombre, habilidad, coste):
        super().__init__(nombre, habilidad, coste)
        
class Mazo:
    def __init__(self) -> None:
        self.cartas = []

    def add_card(self, carta):
        self.cartas.append(carta)

    def show_deck(self):
        for i in self.cartas:
            print(i)



if __name__ == "__main__":
    mazo_heroe = Mazo()
    mazo_heroe.add_card(Oro("Universidad Cosmografia","Oro Inicial. Sólo se pueden buscar y/o Robar cartas por efectos hasta dos veces por turno. Los jugadores deben Desterrar una carta de su mano para jugar una carta sin pagar su coste. Este Oro no puede perder su habilidad."))
    mazo_heroe.add_card(Oro("Hidromiel","Cuando entra en juego, Baraja hasta tres cartas de un Cementerio y Roba dos cartas."))
    mazo_heroe.add_card(Oro("Hidromiel","Cuando entra en juego, Baraja hasta tres cartas de un Cementerio y Roba dos cartas."))
    mazo_heroe.add_card(Oro("Calavera Coronada","Cuando entra en juego, puedes Destruir una carta de coste 1 o menos. Luego, Purifica hasta dos cartas de los Cementerios. Al comienzo de tu Fase Final, puedes Descartar una carta para Robar una carta."))
    mazo_heroe.add_card(Oro("Piedra Cintamani","Si entra en juego en tu primer o segundo turno, busca un Arma, Oro o Tótem en tu Castillo. De lo contrario, Roba una carta. Puedes Desterrarlo para cancelar el ataque oponente."))
    mazo_heroe.add_card(Oro("Piedra Cintamani","Si entra en juego en tu primer o segundo turno, busca un Arma, Oro o Tótem en tu Castillo. De lo contrario, Roba una carta. Puedes Desterrarlo para cancelar el ataque oponente."))
    mazo_heroe.add_card(Oro("Piedra Cintamani","Si entra en juego en tu primer o segundo turno, busca un Arma, Oro o Tótem en tu Castillo. De lo contrario, Roba una carta. Puedes Desterrarlo para cancelar el ataque oponente."))
    mazo_heroe.add_card(Oro("Sigillum Dei", "Puedes Desterrar este Oro de tu Reserva para poner un Oro de tu Castillo en tu Reserva. Cuando pagues el coste de un Aliado con este Oro, puedes Purificar hasta tantas cartas como Fuerza tenga ese Aliado."))
    mazo_heroe.add_card(Oro("Manzanas Doradas","En tu Fase Final, si está en tu Reserva, puedes poner la primer o última carta de tu Castillo en tu mano. Al comienzo de tu Vigilia, si controlas menos Aliados que tu oponente, Genera un Oro para jugar un Arma o Tótem."))
    mazo_heroe.add_card(Oro("Manzanas Doradas","En tu Fase Final, si está en tu Reserva, puedes poner la primer o última carta de tu Castillo en tu mano. Al comienzo de tu Vigilia, si controlas menos Aliados que tu oponente, Genera un Oro para jugar un Arma o Tótem."))
    mazo_heroe.add_card(Oro("Cantar del Mio Cid","Errante. Al comienzo de tu Vigilia, puedes mirar la primera carta de tu Castillo y elegir ponerlo en tu mano o Cementerio. Si controlas más Aliados que tu oponente, en vez de eso puedes subir una carta al azar de tu Cementerio a tu mano."))
    mazo_heroe.add_card(Oro("Dulce Mermelada","Luz. Errante (Sólo puedes controlar una copia de esta carta). Cuando entra en juego, busca un Oro en tu Castillo y ponlo en tu mano. En tu Fase Final, puedes Barajar una carta de tu mano para Agrupar otro Oro que controles."))
    mazo_heroe.add_card(Arma("Dromón Sarraceno","El portador gana 3 de Fuerza. En tu Fase Final, si el portador hace daño de combate puedes agrupar un Aliado y un Oro que controles. Luego, Purifica hasta tantas cartas como fuerza tenga el portador o Roba dos cartas.",1))
    mazo_heroe.add_card(Arma("Guillotina","Maquinaria. Tamaño 1. Gana el control de un Aliado de coste 2 o menos y en tu Fase Final, Destiérralo. Puedes Desterrar una carta de tu Cementerio para subir esta Arma de tu Cementerio a tu mano.",1))
    mazo_heroe.add_card(Arma("Mosquete Nock","Si está en tu Cementerio, puedes pagar un Oro para jugarla. El portador gana 2 de Fuerza, Furia e Imbloqueable. En Asignación de Daño, puedes Purificar hasta tantas cartas como daño haga el portador.",0))
    mazo_heroe.add_card(Arma("Mosquete Nock","Si está en tu Cementerio, puedes pagar un Oro para jugarla. El portador gana 2 de Fuerza, Furia e Imbloqueable. En Asignación de Daño, puedes Purificar hasta tantas cartas como daño haga el portador.",0))
    mazo_heroe.add_card(Arma("Tizona","Errante. El portador gana 2 Fuerza e Indestructible. Cuando entra en juego, Roba una carta. Puedes Desterrarla para Anular un Talismán o cancelar una habilidad oponente.",1))
    mazo_heroe.add_card(Totem("Salem","Tu oponente no puede jugar Talismanes a menos que Destierre dos cartas de su Castillo. Cuando resuelvas un Talismán, puedes Descartar una carta para volver a repetir su efecto. Si Descartaste una Bruja, además puedes Destruir una carta que no sea Oro.",2))
    mazo_heroe.add_card(Totem("Torre de Oro","Cuando entra en juego, Purifica hasta dos cartas de los Cementerios y Roba dos cartas. Puedes Desterrarlo de tu mano o Destruirlo para cambiar los objetivos de un Talismán o habilidad.",1))
    mazo_heroe.add_card(Talisman("Carro de la Muerte","Exhumar. Puedes Desterrar un Oro que controles para jugar este Talismán sin pagar su coste y Destiérralo. Busca un Oro y tu oponente Bota siete cartas.",2))
    mazo_heroe.add_card(Talisman("Bloque de Hielo","En respuesta a que una carta fuera a ser puesta en juego, si no se pagó su coste, puedes poner este Tótem en juego. Cuando entra en juego, Roba dos cartas. No se puede jugar cartas sin pagar su coste ni poner cartas en juego sin pagar su coste.",1))
    mazo_heroe.add_card(Talisman("Oráculo de Delfos","Exhumar. Cuando lo juegues, Destiérralo. Cancela la habilidad de una carta. Este turno, la próxima habilidad que utilice tu oponente de una carta del mismo tipo, cuesta un Oro adicional",1))
    mazo_heroe.add_card(Talisman("Caligrafía","No puede ser Anulado. Anula o Destierra una carta de coste 1 o menos y Roba una carta. Tu oponente puede pagar dos Oros para que este Talismán se resuelva sin efecto.",1))
    mazo_heroe.add_card(Talisman("Caligrafía","No puede ser Anulado. Anula o Destierra una carta de coste 1 o menos y Roba una carta. Tu oponente puede pagar dos Oros para que este Talismán se resuelva sin efecto.",1))
    mazo_heroe.add_card(Talisman("Aliento de Muerte","Destierra un Aliado de tu mano. Luego, Destruye una carta oponente y Roba dos cartas. Si Destruiste un Oro de esta forma tu oponente puede buscar en su Castillo un Oro sin habilidad y ponerlo en su Oro Pagado.",2))
    mazo_heroe.add_card(Talisman("Encuentro de dos Mundos","Sólo puedes jugar Encuentro de dos Mundos por turno y si sólo controlas Aliados. Mira la mano de tu oponente y elige una carta de ahí que no sea Oro. Puedes Desterrarla y Robar dos cartas o jugarla sin pagar su coste. En tu Fase Final, Agrupa un Oro.",1))
    mazo_heroe.add_card(Talisman("Arqueros Letales","Sólo puedes jugar un Arqueros Letales por turno y Destiérralo. Tus Aliados no pueden salir del juego por el turno y Roba una carta por cada Bárbaro, Caballero, Guerrero y/o Héroe que controles. Tu oponente Bota cuatro cartas.",1))
    mazo_heroe.add_card(Talisman("","",))
    mazo_heroe.add_card(Talisman("","",))
    mazo_heroe.add_card(Talisman("","",))
    mazo_heroe.add_card(Talisman("","",))
    mazo_heroe.add_card(Talisman("","",))
    #mazo_heroe.show_deck()
