from Enemigo import*

class ogro(Enemigo):
    def _init_(self, puntos_energia=20, ataque=3):
        super()._init_(tipo_enemigo="ogro", puntos_energia = puntos_energia, ataque=ataque)

    def habla(self):print("Ogro aplastar todo!!!")