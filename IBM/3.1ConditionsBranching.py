a = 6
a == 7 # dará falso porque no es igual 6 a 7
a >= 8 # dará falso también
a != 6 # dará true

# Según el valor de ASCII de las letras:
# ES IMPORTANTE DECIR que cada letra del abecedario tanto mayúscula como minúscula tiene un valor numérico, por lo 
# que sí pueden ser comparadas aún siendo "string" y si se compara un string, su valor se tomará de la primera letra

# Char.	ASCII	Char.	ASCII	Char.	ASCII	Char.	ASCII
#  A	 65	     N	     78	     a	     97	     n	     110
#  B	 66	     O	     79	     b	     98	     o	     111
#  C	 67	     P	     80	     c	     99	     p	     112
#  D	 68	     Q	     81	     d	     100	 q	     113
#  E	 69	     R	     82	     e	     101	 r	     114
#  F	 70	     S	     83	     f	     102	 s	     115
#  G	 71	     T	     84	     g	     103	 t	     116
#  H	 72	     U	     85	     h	     104	 u	     117
#  I	 73	     V	     86	     i	     105	 v	     118
#  J	 74	     W	     87	     j	     106	 w	     119
#  K	 75	     X	     88	     k	     107	 x	     120
#  L	 76	     Y	     89	     l	     108	 y	     121
#  M	 77	     Z	     90	     m	     109	 z	     122


age = int(input("How old are you? "))

if (age >= 18):
    print("You can enter")
else:
    print("Go to see Meat Loaf")
print("Move on")

# OR siempre va a dar True a menos que ambos inputs sean FALSOS porque busca que mínmo o uno U otro sea VERDADERO
# EJEMPLO de True
album_year = 1990
if (album_year < 1980) or (album_year > 1989):
    print("The Album was made in the 70's or 90's")
else:
    print("The Album was made in the 1980's")

# AND es lo contrario, pues ambos inputs tienen que ser VERDADEROS para que dé True, sino siempre dará False
# EJEMPLO de True
album_year1 = 1983
if (album_year1 > 1979) and (album_year1 > 1990):
    print("This Album was made in the 80's")

print("string">"String") # True porque la s minúscula tiene un valor ASCII de 115 y la S mayúscula de 83

# NOT simplemente es lo contrario al input que entra, si es VERDADERO te da un False y si es FALSO da True