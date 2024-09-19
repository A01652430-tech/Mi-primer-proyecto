# Use \n to skip a line when printing strings
# Use \t to insert a Tab when printing strings
# Use \\ doubled to add a \ to the string
import re

salute = "hello everyone"

print(salute[0:4] + " " + salute[10:12])
print(salute[-3:])


# METHODS

# Poner todo en mayúsculas y luego todo en minúsculas
A = "Thriller is the sixth studio album"
B = A.upper()
print(B)
C = B.lower()
print(C)

# Cambiar algo del texto
C = A.replace("Thriller","Bad") # Se pone la primera palabra que tiene el texto "," y la palabra a la que cambiará
print(C)

# Encontrar alguna letra o parte del texto
Name = "Michael Jackson"
print(Name.find("el")) # = 5 pues el "el" se encuentra a partir del sexto caracter
print(Name.find("Jack"))

print(Name[::2]) # Aquí se imprimen uno sí, uno no, es decir, cada segundo número

split_string = (Name.split())
print(split_string) # Aquí se imprimen por separado simplemente

#_________________________________________________________________________________
s1 = "Michael Jackson is the best"
pattern = r"Jackson"

result = re.search(pattern, s1)
if result:
    print("Match found.")
else:
    print("Match not found.")

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # se mostrarán los primeros 10 dígitos consecutivos 
                                   # si se pusiera \D en vez, serían los primeros 10 non-digit characters
text = "My Phone number is 3310209778 and rororororo"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group()) # el .group los agrupa para que no aparezca "3","3","1","0", sino que el número junto
else:
    print("No match")

pattern = r"\W"  # Matches any non-word character te los pone todos
text = "Hello, world!"
matches = re.findall(pattern, text) # Gracias al findall, al parecer el findall es "list" y no se puede .group()

print("Matches:", matches)


s2 = "Michael Jackson was a singer and known as the 'King of Pop'"

# Use the findall() function to find all occurrences of the "as" in the string
results = re.findall("as", s2)

# Print out the list of matched words
print(results)

split_array = re.split("\s", s2) # Te divide toda la oración en palabras por separado
print(split_array)


pattern = r"King of Pop"
replacement = "legend"
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE) # Realmente no sé para qué sirve el flags=re.IGNORECASE
print(new_string)
