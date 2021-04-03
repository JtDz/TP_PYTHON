#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range(4):
    cadena = input("Ingresá una palabra ")
    if "r" in cadena:
        print(f"{cadena} tiene letra r")


# In[ ]:


# desafio 1
for i in range(4):
    cadena = input("Ingresá una palabra ")
    if "r" in cadena:
        print("TIENE R")
    else:
        print("NO TIENE R")


# In[1]:


# desafio 2
for i in range(4):
    cadena = input("Ingresá una palabra ")
    mensaje = "TIENE R" if "r" in cadena else "NO TIENE R"
    print(mensaje)


# In[1]:


#Ingresar palabras desde el teclado hasta ingresar la palabra FIN. 
#Imprimir aquellas que empiecen y terminen con la misma letra.

palabra = input("Ingresar una palabra ")

while palabra != "fin":
    if palabra[0] == palabra[len(palabra)-1]:
        print(palabra)
    palabra = input("Ingresar una palabra ")


# In[1]:


#Necesitamos procesar las notas de los estudiantes de este curso. 
#Queremos saber:
#• cuál es el promedio de las notas;
#• cuántos estudiantes están por debajo del promedio.

lista_notas = []
suma = 0

nota = int(input("Ingresar una nota "))
while nota != -1:
    lista_notas.append(nota)
    suma = suma + nota
    nota = int(input("Ingresar una nota "))
    
prom = suma/len(lista_notas)
cant = 0
for indice in range(len(lista_notas)):
    if lista_notas[indice] < prom:
        cant +=1
print (f'\nLa lista de notas es: {lista_notas}')
print (f'El promedio de notas es: {prom}')
print (f'\nLa cantidad de alumnos con notas bajo el promedio es: {cant}' )


# In[1]:


# Necesitamos procesar las notas de los estudiantes de este curso. 
# Queremos saber:
# - cuál es el promedio de las notas
# - qué estudiantes están por debajo del promedio.


def crear_diccionario():
    """ Retorna un diccionario con los nombres y notas de estudiantes """
    nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    dicci = {}
    while nombre != "FIN":
        nota = int(input(f"Ingresa la nota de {nombre}"))
        dicci[nombre] = nota
        nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    return dicci

def promedio(dicci):
    suma = 0
    for elem in dicci:
        suma = suma + dicci[elem]
    promedio = suma/len(dicci)
    return promedio

dicci = crear_diccionario()
print(dicci)
print(f'\n"El promedio es: {promedio(dicci)}')
print("Los alumnos con notas bajo el promedio son: ")
for elem in dicci:
    if dicci[elem] < promedio(dicci):
        print(elem)
    
        
        
    





# In[ ]:





# In[ ]:




