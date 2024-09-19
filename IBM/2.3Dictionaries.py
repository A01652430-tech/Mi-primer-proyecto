D = {'a':0,'b':1,'c':2} # es un diccionario llamado D que tiene Keys a, b y c con valores 0, 1 y 2 respectivamente
                        # las keys y los valores se separan por :  y finalmente se vuelven como una tabla
print(D["a"]) # pide el valor de la Key a que es 0

print("Todas las keys de D son: ",D.keys()) # pide todas las Keys que hay

print("Todos los valores de las keys de D son: ",D.values()) # pide todos los valores de las Keys que hay

# Los dictionaries pueden tener keys que sean cualquier tipo de data (str, bool, int, float, tuples, etc.) y los valores
# dentro de las keys también pueden ser de cualquier tipo de data.

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict["key1"])
print(Dict[(0,1)])  # aquí imprimirá la 6ta key que es (0, 1) y tiene un valor de 6

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}

print(release_year_dict['The Bodyguard'])

release_year_dict["graduation"] = "2007"    # así se añade una key con su respectivo valor a un dictionary
del(release_year_dict['Thriller'])  # y así se elimina una jey con su respectivo valor de un dictionary
