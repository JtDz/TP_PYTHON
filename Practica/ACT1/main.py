#!/usr/bin/env python
# coding: utf-8

# In[14]:


import string
get_ipython().run_line_magic('run', './funciones.ipynb')

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

#Estructuras-----------------------------------------------------------------------------------------

lista_nombres = formatear_cadena(nombres.split())
lista_1 = [int(elem) for elem in formatear_cadena(eva_1.split('\n'))]
lista_2 = [int(cadena) for cadena in formatear_cadena(eva_2.split('\n'))]
lista_sumas = list(map(sum, zip(lista_1,lista_2)))
matriz = [lista_nombres,lista_1,lista_2,lista_sumas]

#Menu----------------------------------------------------------------------------------------------

cadena1 = '******'*15
cadena2 = '''
              ____________________________MENU INICIAL____________________________
                 Ingrese el NUMERO asociado a la operación que quiera realizar 
              ____________________________________________________________________
              
                                |  1  |  ->  PROMEDIO FINAL
                                |  2  |  ->  REPORTE
                                |  3  |  ->  MOSTRAR TODOS LOS DATOS 
                              
 
         '''

cadena3 = '''

                ____________________________MENU REPORTES___________________________
                    Ingrese el NUMERO asociado al reporte de notas que quiera ver 
                ____________________________________________________________________
                
                                |  1  |  ->  NOTAS DE EVALUACION 1
                                |  2  |  ->  NOTAS DE EVALUACION 2
                                |  3  |  ->  NOTAS FINALES

        '''

cadena4 = '''

                _____________________________MENU LISTAS____________________________
                    Ingrese el NUMERO asociado a la lista que quiera ordenar 
                ____________________________________________________________________
                
                                |  0  |  ->  LISTA DE NOMBRES
                                |  1  |  ->  LISTA DE EVALUACION 1
                                |  2  |  ->  LISTA DE EVALUACION 2
                                |  3  |  ->  LISTA DE NOTAS FINALES
        ''' 
#---------------------------------------------------------------------------------------------------

print(cadena1)
opcion = int(input(cadena2))

if opcion == 1:
    suma = sum(lista_sumas)
    promedio = suma/len(lista_sumas)
    imprimir_datos(lista_nombres, lista_1, lista_2, lista_sumas)
    print ("______________________________________________________________________")
    print ("%-3s%-15s%-15s%+10s%+10s" % ('', '', '', 'Suma: ', suma))
    print ("%-3s%-15s%-15s%-15s%-15s" % ('', '', '', 'Promedio: ', promedio))
    
elif opcion == 2:
    opcion = int(input(cadena3))
    infimo = int(input("Ingresar una nota como cota inferior: "))
    supremo = int(input("Ingresar una nota como cota superior: "))
    dicci_de_listas = dict(zip(matriz[0], matriz[opcion]))
    filtrar_nombres = dict(filter(lambda tupla: tupla[1] >= infimo and tupla[1] <= supremo, dicci_de_listas.items()))
    print(filtrar_nombres)
else:
    opcion = int(input(cadena4))
    lista_ordenada = sorted(matriz[opcion])
    matriz_mod = [[],[],[],[]]
    for lista in matriz:
        if matriz.index(lista) == opcion:
            matriz_mod[opcion] = lista_ordenada
        else:
            matriz_mod[matriz.index(lista)] = modificar_lista(lista, lista_ordenada, matriz[opcion])
    imprimir_datos(matriz_mod[0], matriz_mod[1], matriz_mod[2], matriz_mod[3])
    


# In[ ]:




