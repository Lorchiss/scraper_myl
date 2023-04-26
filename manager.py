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