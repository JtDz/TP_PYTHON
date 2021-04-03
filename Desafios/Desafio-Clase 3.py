#!/usr/bin/env python
# coding: utf-8

# In[1]:


def imprimo(*args):
    """ Esta función imprime los argumentos y sus tipos"""
    for valor in args:
        print(f"{valor} es de tipo {type(valor)}")
imprimo(1)
print("-"*30)
imprimo(2, "hola")
print("-"*30)
imprimo([1,2], "hola", 3.2)
    


# In[3]:


def imprimo_datos(par1, par2, par3):
    print(par2)
lista = [1, 2, 3]
imprimo_datos(*lista)


# In[4]:


def imprimo_agenda(nombre, celu):
    print(nombre, celu)
    
contacto = {"nombre": "frankkaster", "celu": 12345}
imprimo_agenda(**contacto)


# In[10]:


def es_par(x):
    return x%2 == 0
lista = [1, 2, 3, 4, 5, 6, 7]
pares = list(filter(es_par, lista))
print(pares)

def doble(x):
    return 2*x
lista = [1, 2, 3, 4, 5, 6, 7]
dobles = list(map(doble, lista))
print(dobles)

def make_incrementor (n):
    return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)
print (f(42), g(42))
print (make_incrementor(22)(33))


# In[35]:


#26 Cuarto desafío: 

import string
    

def encriptar_letra(letra,cant):
    i = lambda letra, cant: ord(letra) + cant
    
    if  i(letra,cant) > 255:
        letra = char.swapcase()
    else:
        letra = chr(i(letra,cant))
    return letra

def cadena_encriptada(cadena, cant):
    cadena_encrip = ''
    for letra in cadena:
        cadena_encrip += encriptar_letra(letra, cant)
    return cadena_encrip
        
cadena = input("Ingresar una palabra: ")
cant = int(input("Ingresar la cantidad a saltar: "))
print(cadena_encriptada(cadena,cant))


# In[ ]:





# In[ ]:




