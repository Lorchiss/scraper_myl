import random
import os 
import copy 

class Carta:
    def __init__(self, nombre, habilidad, tipo=None):
        self.nombre = nombre
        self.habilidad = habilidad
        self.tipo = tipo
    
    def __str__(self) -> str:
        return (f"Oro       - {self.nombre} ")
    
    

class Oro(Carta):
    def __init__(self, nombre, habilidad):
        super().__init__(nombre, habilidad, tipo='Oro')


class Aliado(Carta):
    def __init__(self, nombre, habilidad, fuerza, coste):
        super().__init__(nombre, habilidad, tipo='Aliado')
        self.fuerza = fuerza
        self.coste = coste

    def __str__(self) -> str:
        return (f"{self.tipo}   - {self.nombre} ({self.coste}) (f {self.fuerza})")

class ATT(Carta):
    def __init__(self, nombre, habilidad, coste,tipo):
        super().__init__(nombre, habilidad,tipo)
        self.coste = coste

    def __str__(self) -> str:
        return (f"{self.tipo}   - {self.nombre}  ({self.coste}) ")

class Arma(ATT):
    def __init__(self, nombre, habilidad, coste):
        super().__init__(nombre, habilidad, coste, tipo='Arma')

class Totem(ATT):
    def __init__(self, nombre, habilidad, coste):
        super().__init__(nombre, habilidad, coste, tipo='Totem')

class Talisman(ATT):
    def __init__(self, nombre, habilidad, coste):
        super().__init__(nombre, habilidad, coste, tipo='Talisman')
        
class Mazo:
    def __init__(self) -> None:
        self.cartas = [] 
        self.oro_inicial = None
        self.mulligan = 8
        self.mano = []

    #Mostrar
    def __str__(self) -> str:
        return self.cartas

    def show_deck(self, conjunto):
        os.system("cls")
        for carta in conjunto:
            print(carta)
    

    #Setear
    def set_mulligan(self):
        self.mulligan -= 1

    def add_oro_inicial(self,oro):
        self.oro_inicial = oro

    def add_card(self, carta):
        if self.count() <= 48:
            self.cartas.append(carta)
        else:
            print ("Mazo completo!")

    #Getter
    def count(self) -> int:
        return len(self.cartas)

    #Function            
    def mezclar_mazo(self):
        random.shuffle(self.cartas)

    def robar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop(0)
        else:
            print("El mazo está vacío.")

    def draw_mano_inicial(self):
        self.mano = [self.robar_carta() for i in range(self.mulligan)] 
        #self.show_deck(self.mano)
        return self.mano
        # while self.do_mulligan():
        #     self.mano = [self.robar_carta() for i in range(self.mulligan)] 
        #     self.show_deck(self.mano)

    def do_mulligan(self):
        mulligan = input("¿Quieres hacer mulligan? (s/n) ")
        if mulligan.lower() == "s":
            for i in range(self.mulligan):
                print(i)
                carta = self.mano.pop(0)
                self.add_card(carta)
                print(f"Descartando carta {carta}")
            self.set_mulligan()
            return True
        else:
            return False

    def copy(self):
        new_deck = Mazo()
        new_deck.cartas = copy.deepcopy(self.cartas)
        new_deck.oro_inicial = copy.deepcopy(self.oro_inicial)
        new_deck.mulligan = copy.deepcopy(self.mulligan)
        new_deck.mano = copy.deepcopy(self.mano)
        return new_deck


    