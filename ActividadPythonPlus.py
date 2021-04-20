#!/usr/bin/env python
# coding: utf-8

# In[6]:


from collections import Counter
import csv

archivo = open("\\Users\\pc\\OneDrive\\Escritorio\\Python2021\\appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',') 

encabezado = csvreader.__next__()
encabezado = next(csvreader)

print(encabezado)

lista_num_votes = []
for linea in csvreader:
    if linea[5] <= 3 and linea[17] == "Card Game":
        print(f"Nombre: {linea[3]:<40}")
    elem = (linea[12],linea[13])
    lista_num_votes.append(elem)
archivo.close()


objetoCounter = Counter(lista_num_votes)
print(objetoCounter.most_common(10))


# In[ ]:




