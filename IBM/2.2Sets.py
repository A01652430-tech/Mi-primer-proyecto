music = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco" } # los valores que se repiten como "rock"
                                                                              # no se toman en cuenta más de una vez
soda_list = ["coca cola", "fanta", "pepsi"]
soda_set = set(soda_list) # se convierte una lista en un Set

A = {"AC/DC", "Back in Black", "Thriller"}
A.add("NSYNC")  # para añadir algo a un set
print(A)
print(type(A))

A.remove("NSYNC") # para quitar algo del set

print("AC/DC" in A) # para saber si hay algo contenido en el set
album_set1 = {"AC/DC", "Back in Black", "Thriller"}
album_set2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}

album_set3 = album_set1 & album_set2 # para saber cuáles contenidos están en un album y también en el otro (repetidos)
print(album_set3)
print(album_set1.intersection(album_set2)) # también se podría obtener el mismo resultado así

album_set_1 = {"AC/DC", "Back in Black", "Thriller"}
album_set_2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}
print(album_set_1.union(album_set_2))   # la unión de lo que tienen los dos juntos completos

perros = {"Maya", "Jack", "Lucky", "Max"}
perros2 = {"Maya", "Max"}

print(perros2.issubset(perros))  # para saber si perros2 (todos los elementos) está contenido dentro de perros 

print(perros.issuperset(perros2))  # para saber si perros tiene dentro todos los elementos de perros2

print(perros.difference(perros2))   # para saber qué valores tiene de diferentes perros a perros2