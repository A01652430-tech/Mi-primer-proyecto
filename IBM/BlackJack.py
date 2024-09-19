import random

print("This is")
print("""
 ____  _            _        _            _    
|  _ \| |          | |      | |          | |   
| |_) | | __ _  ___| | __   | | __ _  ___| | __
|  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
| |_) | | (_| | (__|   < |__| | (_| | (__|   < 
|____/|_|\__,_|\___|_|\_\____/ \__,_|\___|_|\_\      
    
""")

A = 11
J = 10
Q = 10
K = 10

cartasPosibles = [A,"2","3","4","5","6","7","8","9","10",J,Q,K]
cartasRandom = random.choice(cartasPosibles)
cartasRandom2 = random.choice(cartasPosibles)
cartasRandom3 = random.choice(cartasPosibles)
cartasRandom4 = random.choice(cartasPosibles)
cartasRandom5 = random.choice(cartasPosibles)

nuevoJuego = print("Estas son tus cartas",cartasRandom,cartasRandom2)


puntuación = int(cartasRandom) + int(cartasRandom2)
print("Tu suma actual es: ",puntuación)

print("¿Quieres otra carta?")
respuesta1 = input().lower()
noVariaciones = ["no","nop","noup"]
siVariaciones = ["si","sí","sip","yes"]

if respuesta1 in noVariaciones:
    print("Perfecto, tu puntuación fue de: ",puntuación)
elif respuesta1 in siVariaciones:
    print(cartasRandom3) 
    puntuación2 = puntuación + int(cartasRandom3)
    print("Tu suma actual es:",puntuación2)
    print("¿Quieres otra carta?")
    respuesta2 = input().lower()
    if respuesta2 in noVariaciones:
        print("Perfecto, tu puntuación fue de: ",puntuación2)
    elif respuesta2 in siVariaciones:
        print(cartasRandom4)
        puntuación3 = puntuación2 + int(cartasRandom4)
        print("Tu suma actual es:",puntuación3)
        print("¿Quieres otra carta?")
        respuesta3 = input().lower()
        if respuesta3 in noVariaciones:
            print("Perfecto, tu puntuación fue de: ",puntuación3)
        elif respuesta2 in siVariaciones:
            print(cartasRandom5)
            puntuación4 = puntuación3 + int(cartasRandom5)
            print("Tu suma actual es:",puntuación4)
            print("¿Quieres otra carta?")
        