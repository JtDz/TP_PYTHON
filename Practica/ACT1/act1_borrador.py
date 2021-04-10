#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
import statistics

nombres  = """
    "Agustin",
    "Alan",
    "Andrés",
    "Ariadna",
    "Bautista",
    "CAROLINA",
    "CESAR",
    "David",
    "Diego",
    "Dolores",
    "DYLAN",
    "ELIANA",
    "Emanuel",
    "Fabián",
    "Facundo",
    "Facundo",
    "FEDERICO",
    "FEDERICO",
    "GONZALO",
    "Gregorio",
    "Ignacio",
    "Jonathan",
    "Jonathan",
    "Jorge",
    "JOSE",
    "JUAN",
    "Juan",
    "Juan",
    "Julian",
    "Julieta",
    "LAUTARO",
    "Leonel",
    "LUIS",
    "Luis",
    "Marcos",
    "María",
    "MATEO",
    "Matias",
    "Nicolás",
    "NICOLÁS",
    "Noelia",
    "Pablo",
    "Priscila",
    "TOMAS",
    "Tomás",
    "Ulises",
    "Yanina",
"""
eva_1 = """
 81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
"""
eva_2 = """
 30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10"""

def normalize(cadena):
    '''reemplaza una vocal con tilde por un sin tilde'''
    reemplazar = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in reemplazar:
        cadena = cadena.replace(a, b)
    return cadena


def formatear_cadena(lista):
    '''corrige cadena de caracteres de una lista para poder operar con ella'''
    
    newlist = []
    for elem in lista:
        elem = normalize(elem).lower()
        car = '",\' '
        nom = ''
        for letra in elem:
            if letra not in car:
                nom  += letra
        newlist.append(nom)
    if newlist[0] == '':
        newlist.remove(newlist[0])
    if newlist[len(newlist)-1] == '':
        newlist.remove(newlist[len(newlist)-1])
        
    return newlist


lista_nombres = formatear_cadena(nombres.split())
lista_1 = [int(elem) for elem in formatear_cadena(eva_1.split('\n'))]
lista_2 = [int(cadena) for cadena in formatear_cadena(eva_2.split('\n'))]

#Promedio______________________________________________________________________________________________________________

lista_sumas = list(map(sum, zip(lista_1,lista_2)))
promedio = statistics.mean(lista_sumas)
print(f'El promedio de la suma de las notas es {primedio}')

#Reporte______________________________________________________________________________________________________________

matriz = [lista_nombres,lista_1,lista_2,lista_sumas]

opcion = int(input("Ingresar la opción que contiene la lista a acotar: "))
infimo = int(input("Ingresar una cota inferior para el rango: "))
supremo = int(input("Ingresar un cota superior para el rango: "))


dicci_de_listas = dict(zip(matriz[0], matriz[opcion]))
filtrar_nombres = dict(filter(lambda tupla: tupla[1] >= infimo and tupla[1] <= supremo, dicci_de_listas.items()))
print(filtrar_nombres)
                       
#Ordenar________________________________________________________________________________________________________________

opcion = int(input("Ingresar la opción que contiene la lista a ordenar: "))

lista_ordenada = sorted(matriz[opcion])

def modificar_lista(lista):
    '''Devuelve una nueva lista con sus elementos modificados de acuerdo a una lista previamente ordenada '''
    lista_mod = []
    for elem in lista_ordenada:
        i = 0
        while elem != matriz[opcion][i]:
            i += 1
        lista_mod.append(lista[i])    
    return lista_mod

matriz_mod = [[],[],[],[]]

for lista in matriz:
    if matriz.index(lista) == opcion:
        matriz_mod[opcion] = lista_ordenada
    else:
        matriz_mod[matriz.index(lista)] = modificar_lista(lista)
        
        
print ("%-3s%-15s%-15s%-15s%-15s" % ('', 'Nombre', 'Evacualción 1', 'Evaluació 2', 'Total'))
print ("___________________________________________________________________________________") 
i = 0
while i < len(matriz_mod[0]):
    print ("%-3s%-15s%8s%13s%13s" % (i, matriz[0][i].capitalize(), matriz_mod[1][i], matriz_mod[2][i], matriz_mod[3][i]))
    i += 1

