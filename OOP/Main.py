from Enemigo import *
from Zombie import *
from Ogro import *

Zombie = Zombie(10, 1)
Ogro = Ogro(20, 3)

def batalla(e1: Enemigo, e2 : Enemigo):
    e1.habla()
    e2.habla()

    while e1.puntos_energia > 0 and e2.puntos_energia > 0:
        print("#############")
        e1.ataque_especial()
        e2.ataque_especial()
        print(f"{e1.get_tipo_enemigo()}: quedan: {e1.puntos_energia} puntos de energia")
        print(f"{e2.get_tipo_enemigo()}: quedan: {e2.puntos_energia} puntos de energia")
        print(f"ataque: {e2.ataque}")
        e1.puntos_energia -= e2.ataque
        print("===================")
        print(f"ataque: {e1.ataque}")
        e2.puntos_energia -= e1.ataque

        print("############")
        if e1.puntos_energia > 0:
            print(f"{e1.get_tipo_enemigo()} gano")
        else:
            print(f"{e2.get_tipo_enemigo()} gano")

print("============BATALLA============")
batalla(Zombie, Ogro)
print("============FIN DE LA BATALLA============")
#print(f"{Zombie.get_tipo_enemigo()} tiene {Zombie.puntos_energia} de energia y ataca con {Zombie.ataque}")
#print(f"{Ogro.get_tipo_enemigo()} tiene {Ogro.puntos_energia} de energia y ataca con {Ogro.ataque}")