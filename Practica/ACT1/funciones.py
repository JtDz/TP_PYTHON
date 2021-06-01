#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


def modificar_lista(lista, lista_ordenada, lista_no_ordenada):
    '''Devuelve una nueva lista con sus elementos modificados de acuerdo a una lista previamente ordenada '''
    lista_mod = []
    for elem in lista_ordenada:
        i = 0
        while elem != lista_no_ordenada[i]:
            i += 1
        lista_mod.append(lista[i])    
    return lista_mod
        
        
def imprimir_datos(lista_nom, lista_eva1, lista_eva2, lista_sum):
    
    '''Muestra los datos por pantalla en una tabla'''
    
    print ("%-3s%-15s%-15s%-15s%-15s" % ('', 'Nombre', 'Evacualción 1', 'Evaluació 2', 'Total'))
    print ("___________________________________________________________________________________") 
    i = 0
    while i < len(lista_nom):
        print ("%-3s%-15s%8s%13s%13s" % (i, lista_nom[i].capitalize(), lista_eva1[i], lista_eva2[i], lista_sum[i]))
        i += 1

