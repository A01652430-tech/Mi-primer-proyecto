# Tuples are an order sequence in parenthesis and each value is separated by commas
# Tuples can contain inside any type of variables (int, float, bool, or str)

grupo1 = (4,10,1.2)
print(grupo1[0]) # que es igual a print(grupo1[-3])
print(grupo1[1]) # que es igual a print(grupo1[-2])
print(grupo1[2]) # que es igual a print(grupo1[-1])

grupo2 = grupo1 + ("hard rock",10) # También se pueden añadir cosas

print(grupo2[3:5]) # Se pueden imprimir los valores en conjunto, el número que pides siempre será uno más del que quieres
                   # Es decir, yo quiero el valor 3 y 4, entonces pido del 3:5

grupoSorteado = sorted(grupo1) # Aquí los ordena de menor a mayor
print(grupoSorteado)

NT = (1,2,("pop","rock"),(3,4),("disco",(1,2))) # Puedes tener grupos dentro de tu Tuple y se llama Nesting
print(NT[2][1]) # También acceder a cada parte específicamente
print(len(NT))
print(NT[2][1][0]) # Se puede acceder a una letra nada más también


# Lists are an order sequence in Corchetes and each value is separated by commas
# Lists can contain inside any type of variables (int, float, bool, or str)

L = ["Michael Jackson", 10.1, 1982]
L.extend(["pop",10])
print(L)            # En este caso se sumarían y la lista quedaría así ["Michael Jackson", 10.1, 1982,"pop",10]

L.append(["pop",10])
print(L)            # Ahora la lista sería así ["Michael Jackson", 10.1, 1982,["pop",10]] con lo añadido separado

A = ["Disco",10,1.2]
A[0] = "Hard rock"    # Para cambiar cosas de la lista es tan simple como poner el lugar en el que está = lo que quieres

del(A[0])    # Borrar también es sencillo, solo se pone del al principio y el lugar de lo que borrarás

nl = "hard rock".split() # Se puede cambiar una palabra con .split a una lista -> ["hard","rock"]
print(nl)

nl2 = "A.B.CC .   D".split(".") # Aquí separas todo lo que está separado por puntos
print(nl2)

nl = A[:] # Esto hace que ahora nl va a tener una copia de lo que tiene A, pero si cambias algo de A nl no lo tendrá
          # cambiado  como pasaría si no pusieras los [:]

B = ["a","b","c"]
print(B[1:])

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
print(genres_tuple.index("disco"))  # El .index te dice en qué lugar de la Tuple o List está lo que buscas (solo el primero que aparece)
