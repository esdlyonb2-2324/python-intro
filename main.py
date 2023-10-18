import wordies

import random

from bidules import machins

import math


print(random.randint(2, 7))

print(machins.choses)

machins.fais_un_truc()



dauphin = "voila un dauphin"

print(dauphin)

number = 12

number_float = 12.346578657

#print(dauphin[1])

list = ["truc", "machin", 12, "chaussette"]

for list in range(1, 4):
    print('coucou')


# print(list[1:3])

dictionary = {
    "name": "luc",
    "surname": "dupont",
    "bordel": {
        "truc": "blablabla"
    }

}

#print(dictionary["bordel"]["truc"])

truc_tuple = (1, 2)

truc_boolean = True

def fais_des_pates():
    print("spaghetti")

#print("ravioli")

# reponse = input("t'aimes le veau ?")
#
# print("ta réponse est :"+reponse)

#print("4"+4)

print(wordies.words)


question = input("tu veux la racine carrée de combien ?")

nombre = int(question)

try:
    square_root = math.sqrt(nombre)
    print("la racine carree est : ")
    print(square_root)
except ValueError:
    print('donne moi un nombre positif, banane')
finally:
    print('et voila on a fini')

