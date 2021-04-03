#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dado un caracter ingresado por el teclado, queremos saber si es una comilla o no.
caracter = input("Ingresar un carácter cualquiera ")
if ("\"" == caracter):
    print("Es una comilla \"")
else:
    print("No es comilla")


# In[1]:


# Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que tenga más caracteres.
cadena_1=input("Ingresar una palabra ")
cadena_2=input("Ingresar otra palabra ")
if (len(cadena_1) > len(cadena_2)):
    print(cadena_1 + " es la más larga")
else:
    print(cadena_2 + " es la más larga")


# In[1]:


# Ingrese desde teclado una cadena de caracteres e imprima cuántas letras “a” contiene.
cadena_1=input("Ingresar una palabra ")
cant = 0
for letra in cadena_1:
    if (letra == "a"):
        cant = cant + 1
print (cant)


# In[ ]:




