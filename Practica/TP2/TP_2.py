#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.- Tomando el texto del README.md de numpy, imprima todas las líneas que contienen ‘http’ o ‘https’.

numpy_readme = """"¡El proyecto NumPy agradece su experiencia y entusiasmo!

Siempre se agradecen las pequeñas mejoras o correcciones; los temas etiquetados como "buen primer número" pueden ser un buen punto de partida. Si está considerando más contribuciones grandes al código fuente, comuníquese con nosotros a través de la lista de correo primero.

Escribir código no es la única forma de contribuir a NumPy. Tú también puedes:

revisar solicitudes de extraccion
problemas de triaje
Desarrollar tutoriales, presentaciones y otros materiales educativos.
mantener y mejorar nuestro sitio web
Desarrollar diseño gráfico para los activos de nuestra marca y materiales promocionales.
traducir el contenido del sitio web
ayudar con la divulgación y la incorporación de nuevos contribuyentes
escribir propuestas de subvenciones y ayudar con otros esfuerzos de recaudación de
Si no está seguro de por dónde empezar o cómo encajan sus habilidades, ¡comuníquese! Puede preguntar en la lista de correo o aquí, en GitHub, abriendo una nueva edición o dejando un comentario sobre una cuestión relevante que ya está abierta.

Nuestros Canales de Comunicación Preferidos TODOS hijo Públicos, Pero si DESEA Primero Hablar Con Nosotros En Privado, comuniquese con Nuestros Coordinadores de la Comunidad en numpy-team@googlegroups.com o en Slack (Escribá un numpy-team@googlegroups.com párrafo Recibir Una invitación).

También tenemos una llamada comunitaria quincenal, cuyos detalles se anuncian en la lista de correo. Le invitamos a unirse.

Si es nuevo en la contribución al código abierto, esta guía le ayudará a explicar por qué, qué y cómo participar con éxito."""

#Convertir el string en una lista de oraciones con .split('\n') o .splitline 
lista = numpy_readme.splitlines()
print(lista)

#OPCION 1: Recorremos con un for.
for line in lista:
    if ('htt' in line):
        print(line)
        
    
#OPCION 2: Crear una lista con la condicion e imprimirla 
lista_htt = []
for line in lista:
    if ('htt' in line):
        lista_htt.append(line)
print(lista_htt)

#OPCION 3: Crear lista por comprension e imprimirla. La más visual de todas

lista_htt = [line for line in lista if 'htt' in line]
print(lista_htt)

#--------------------------------------------------------------------------------------------------------------------------

# 2. Indique la palabra que aparece mayor cantidad de veces en el texto del README.md de numpy.

wordlist = numpy_readme.split(' ')
print (wordlist)

def most_frequency_word(wordlist):
    dicci = {} 
    for word in wordlist:
        dicci[word] = wordlist.count(word)
    max_word=' '
    max = -1
    for word in dicci:
        if dicci[word] > max:
            max_word = word
            max = dicci[word]
    return max_word

print(f'La palabra más frecuente es: {most_frequency_word(wordlist)}')
        
    


# In[10]:


import pandas as pd
# Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
#letra. En caso que no se haya inrgesado un letra, indique el error. 

texto = """Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido.
También es una composición de caracteres imprimibles generados por un algoritmo de cifrado que, aunque no tienen sentido 
para cualquier persona, sí puede ser descifrado por su destinatario original."""

lista = texto.split(' ')
palabra = input("Ingrese una palabra cualquiera ")           
palabra = palabra.lower()
if palabra.isalpha(): 
    #Crea e imprime lista con elementos no repetidos.
    #Más opciones en:https://www.analyticslane.com/2020/06/29/truco-python-eliminar-los-valores-duplicados-de-una-lista-en-python/
    wordlist_1 = [word for word in lista if word[0] == palabra[0]]
    print(pd.unique(wordlist_1))    
else:
    print("No es una PALABRA")







# In[2]:


#ejercicio 4

cadena = input("Ingresa una clave que no tenga @ o ! y sean menos de 10 caracteres: ")

if len(cadena) >= 10:
    print("Son más de 10 caracteres -.-")
if cadena.find('@') != -1 or cadena.find('!') != -1:
    print("La clave ingresada tiene @ o !")


# In[7]:


#5. Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras,
#y sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir
#entre mayúsculas y minúsculas.

frase = input("Ingrese una frase cualquiera ").lower()  
lista = frase.split(' ')

palabra = input("Ingrese una palabra cualquiera ").lower
frecuencia = lista.count(palabra)
print (f'La palabra ingresada tiene una frecuencia de {frecuencia} en la frase ingresada')


# In[11]:


#6. Dada una frase donde las palabras pueden estar repetidas e indistintamente en mayúsculas y
#minúsculas, imprimir una lista con todas las palabras sin repetir y en letra minúscula.
import pandas as pd

frase = """
    Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
    automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
    reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
    un montón de archivos con fotos de una manera compleja. Tal vez quieras
    escribir alguna pequeña base de datos personalizada, o una aplicación
    especializada con interfaz gráfica, o UN juego simple.
"""
frase_minuscula = frase.lower()
lista = frase_minuscula.split()
print(pd.unique(lista))


# In[11]:


#7. Trabajando con los contenidos de los archvios que pueden acceder en el curso:
#    • nombres
#    • eval1
#    • eval2
#   Copiar el contenido de los archvios en variables de tipo string y realizar.
#    • generar una estructura con los nombres de los estudiantes y la suma de ambas.
#    • Calcular el promedio de las notas totales e informar quiénes obtuvieron menos que el promedio.
#    notas.

import string
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

#---------------------------------------------------------------------------------------
#Funcion para dar formato a los nombres y enteros  
def formatear_cadena(lista):
    newlist = []
    for elem in lista:
        car = '", '
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

#Convierto las listas de str a una lista de int-------------------------------------

lista = eva_1.split('\n')
lista_1 = [int(elem) for elem in formatear_cadena(lista)]

lista = eva_2.split('\n')
lista_2 = [int(cadena) for cadena in formatear_cadena(lista)]

# Crear lista con la suma de eva1+eva2
lista_total = []
for e1, e2 in zip(lista_1, lista_2):
    lista_total.append(e1+e2)
    
#Crear lista de nombres
lista = nombres.split()
lista_nombres = [cadena for cadena in formatear_cadena(lista)]

#Diccionario con los nombres y la suma de eva1 y eva2
dicci = {}
for nombre, nota in zip(lista_nombres, lista_total):
    dicci[nombre] = nota
print(dicci.items())

#Calcular e informar promedio
suma = 0
for nombre in dicci:
    suma = suma + dicci[nombre]    
promedio = suma/len(dicci)
print(f'El promedo es {promedio}')

#Imprime nombres con la consicion y promedio. esta ofe, sip.
for nombre in dicci:
    if dicci[nombre] < promedio:
        print(f'{nombre.capitalize()} tiene un promedio de: {dicci[nombre]}')


# In[25]:


#8. CONSULTAR COMO CENTRAR LOS ENTEROS
#Con la información de los archivos de texto que se encuentran disponibles en el curso:
#    • nombres_1
#    • nombres_2
#Nota: Trabaje con los datos en variables de tipo string.
#    • Indique los nombres que se encuentran en ambos. Nota: pruebe utilizando list comprehension.
#    • Genere dos variables con la lista de notas que se incluyen en los archivos: eval1.txt y eval2.txt
#      e imprima con formato los nombres de los estudiantes con las correspondientes nota y la suma
#      de ambas como se ve en la imagen:
import string
import pandas as pd

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

nombre1 = """
 'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'
"""
nombre2 = """
 'Agustin',
 'AGUSTIN',
 'Agustín',
 'Ailen',
 'Alfredo',
 'Amalia',
 'Ariana',
 'Bautista',
 'Braian',
 'Carla',
 'CESAR',
 'Daniel',
 'Diego',
 'ELIANA',
 'Facundo',
 'Facundo',
 'Facundo',
 'Facundo',
 'Federico',
 'Federico',
 'Flavia',
 'Francisco',
 'Germán',
 'Guido',
 'GUSTAVO',
 'Hilario',
 'Ignacio',
 'IVAN',
 'Jimmy',
 'Joaquín',
 'Jose',
 'Josue',
 'JUAN',
 'Juan',
 'Laura',
 'LAURA',
 'Lautaro',
 'Lautaro',
 'Ludmila',
 'Marcos',
 'Marcos',
 'MARIANELA',
 'MARTIN',
 'MATEO',
 'Mateo',
 'Matias',
 'MAURO',
 'Maximiliano',
 'NESTOR',
 'Nicolas',
 'Pedro',
 'Ramiro',
 'Sofía',
 'Tobias',
 'Tomás',
 'Tomás',
 'Ulises',
 'Yanina'
"""
#Funcion para reemplazar una vocal con tilde por un sin tilde-----------------------------------------------
def normalize(cadena):
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

#Funcion para dar formato a los nombres y enteros------------------------------------------------------
def formatear_cadena(lista):
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

#Convierto las listas de str a una lista de int-------------------------------------

lista = eva_1.split('\n')
lista_1 = [int(elem) for elem in formatear_cadena(lista)]

lista = eva_2.split('\n')
lista_2 = [int(cadena) for cadena in formatear_cadena(lista)]

# Crear lista con la suma de eva1+eva2-------------------------------------------------
lista_total = []
for e1, e2 in zip(lista_1, lista_2):
    lista_total.append(e1+e2)
    
#Crear lista de nombres---------------------------------------------------------------
lista = nombres.split()
lista_nombres = formatear_cadena(lista)

#Crear listas con nombres no repetidos-------------------------------------------------

lista = nombre1.split()
lista1 = formatear_cadena(lista)
lista1 = pd.unique(lista1)


lista = nombre2.split()
lista2 = formatear_cadena(lista)
lista2 = pd.unique(lista2)

# Habia que hacerlo con lista por comprensión pero no sé como sería :c----------------------------------
repetidos = []
for nom1 in lista1:
    for nom2 in lista2:
        if nom1 == nom2:
            repetidos.append(nom1.capitalize())
#print(repetidos)

# El desafio de la bidah--------------------------------------------------------------

i = 0
print ("%-3s%-15s%-15s%-15s%-15s" % ('', 'Nombre', 'Evacualción 1', 'Evaluació 2', 'Total'))
while i < len(lista_nombres):
    print ("%-3s%-15s%-15s%-15s%-15s" % (i, lista_nombres[i], lista_1[i] , lista_2[i], lista_total[i]))
    i += 1





# In[28]:


#9. Escbriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
#misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
#inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
#es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres


#Funcion heterograma
def heterograma_detector(lista):
    exito = True
    indice_lista = 0
    while indice_lista < len(lista) and exito:
        indice_letra = 0
        while lista[indice_lista].isalpha() and indice_letra < len(lista[indice_lista]):
            indice_letra += 1
        if lista[indice_lista].isalpha():
            exito = False
        indice_lista += 1
    return exito

cadena = input("Ingresar una palabra o frase: ").lower()
lista = cadena.split(' ')
if heterograma_detector(lista):
    print("SI ES")
else:
    print("NO ES")

                            


# In[30]:


# CONSULTAR PORQUE NO ME TOMA LA U!!!!!!!
#Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada
#la siguiente tabla de valores del juego Scrabble

#Crear diccionario___________________________________________________________________________________

dicci = {}
cadena = "A B C D E F G H I J L M N O P Q R S T W X Y Z"
lista = cadena.split()
for letra in lista:
    if letra in "AEIOULNRST":
        dicci[letra] = 1
    elif letra in "DG":
        dicci[letra] = 2
    elif letra in "BCMP":
        dicci[letra] = 3
    elif letra in "FHVWY":
        dicci[letra] = 4
    elif letra in "K":
        dicci[letra] = 5
    elif letra in "JX":
        dicci[letra] = 8
    elif letra in "QZ":
        dicci[letra] = 10
#print(dicci)        

palabras = input("Escriba una palabra o frase que no tenga U: ").upper()
lista = palabras.split()

# suma puntos_______________________________________________________________________________________________
suma = 0
for palabra in lista:
    for letra in palabra:
        suma = suma + dicci[letra]
print (f'La palabra {palabras} tiene {suma} puntos')
        


# In[8]:


#11.CONSULTAR SI LO QUE HICE ES LO QUE PiDeN
#¿Conoces Pypi? Es un sitio con gran variedad de librerías que podés instalar libremente a
#través de la herramienta pip. Te permite buscar proyectos según el área de interés. Queremos
#procesar esta lista de categorías como un string para poder saber las subcategorías tiene cada
#una. Copia el contenido del archivo categorias como contenido de una variable string para
#poder obtener información de la cantidad de subcategorías y la lista que incluye cada categoría

import string

cadena = """
ptive Technologies
Artistic Software
Communications

    BBS
    Chat
        ICQ
        Internet Relay Chat
        Unix Talk 
    Conferencing
    Email
        Address Book
        Email Clients (MUA)
        Filters
        Mail Transport Agents
        Mailing List Servers
        Post-Office
            IMAP
            POP3 
    FIDO
    Fax
    File Sharing
        Gnutella 
    Ham Radio
    Internet Phone
    Telephony
    Usenet News 

Database

    Database Engines/Servers
    Front-Ends 

Desktop Environment

    File Managers
    GNUstep
    Gnome
    K Desktop Environment (KDE)
    Screen Savers
    Window Managers
        Blackbox
        Fluxbox
        XFCE 

Documentation

    Sphinx 

Education

    Computer Aided Instruction (CAI)
    Testing 

Games/Entertainment

    Arcade
    Board Games
    First Person Shooters
    Fortune Cookies
    Multi-User Dungeons (MUD)
    Puzzle Games
    Real Time Strategy
    Role-Playing
    Side-Scrolling/Arcade Games
    Simulation
    Turn Based Strategy 

Home Automation
Internet

    File Transfer Protocol (FTP)
    Finger
    Log Analysis
    Name Service (DNS)
    Proxy Servers
    WAP
    WWW/HTTP
        Browsers
        Dynamic Content
            CGI Tools/Libraries
            Content Management System
            Message Boards
            News/Diary
            Page Counters
            Wiki 
        HTTP Servers
        Indexing/Search
        Session
        Site Management
            Link Checking 
        WSGI
            Application
            Middleware
            Server 
    XMPP
    Z39.50 

Multimedia

    Graphics
        3D Modeling
        3D Rendering
        Capture
            Digital Camera
            Scanners
            Screen Capture 
        Editors
            Raster-Based
            Vector-Based 
        Graphics Conversion
        Presentation
        Viewers 
    Sound/Audio
        Analysis
        CD Audio
            CD Playing
            CD Ripping
            CD Writing 
        Capture/Recording
        Conversion
        Editors
        MIDI
        Mixers
        Players
            MP3 
        Sound Synthesis
        Speech 
    Video
        Capture
        Conversion
        Display
        Non-Linear Editor 

Office/Business

    Financial
        Accounting
        Investment
        Point-Of-Sale
        Spreadsheet 
    Groupware
    News/Diary
    Office Suites
    Scheduling 

Other/Nonlisted Topic
Printing
Religion
Scientific/Engineering

    Artificial Intelligence
    Artificial Life
    Astronomy
    Atmospheric Science
    Bio-Informatics
    Chemistry
    Electronic Design Automation (EDA)
    GIS
    Human Machine Interfaces
    Hydrology
    Image Processing
    Image Recognition
    Information Analysis
    Interface Engine/Protocol Translator
    Mathematics
    Medical Science Apps.
    Physics
    Visualization 

Security

    Cryptography 

Sociology

    Genealogy
    History 

Software Development

    Assemblers
    Bug Tracking
    Build Tools
    Code Generators
    Compilers
    Debuggers
    Disassemblers
    Documentation
    Embedded Systems
    Internationalization
    Interpreters
    Libraries
        Application Frameworks
        Java Libraries
        PHP Classes
        Perl Modules
        Pike Modules
        Python Modules
        Ruby Modules
        Tcl Extensions
        pygame 
    Localization
    Object Brokering
        CORBA 
    Pre-processors
    Quality Assurance
    Testing
        Acceptance
        BDD
        Mocking
        Traffic Generation
        Unit 
    User Interfaces
    Version Control
        Bazaar
        CVS
        Git
        Mercurial
        RCS
        SCCS 
    Widget Sets 

System

    Archiving
        Backup
        Compression
        Mirroring
        Packaging 
    Benchmark
    Boot
        Init 
    Clustering
    Console Fonts
    Distributed Computing
    Emulators
    Filesystems
    Hardware
        Hardware Drivers
        Mainframes
        Symmetric Multi-processing
        Universal Serial Bus (USB) 
    Installation/Setup
    Logging
    Monitoring
    Networking
        Firewalls
        Monitoring
            Hardware Watchdog 
        Time Synchronization 
    Operating System
    Operating System Kernels
        BSD
        GNU Hurd
        Linux 
    Power (UPS)
    Recovery Tools
    Shells
    Software Distribution
    System Shells
    Systems Administration
        Authentication/Directory
            LDAP
            NIS 

Terminals

    Serial
    Telnet
    Terminal Emulators/X Terminals 

Text Editors

    Documentation
    Emacs
    Integrated Development Environments (IDE)
    Text Processing
    Word Processors 

Text Processing

    Filters
    Fonts
    General
    Indexing
    Linguistic
    Markup
        HTML
        LaTeX
        Markdown
        SGML
        VRML
        XML
        reStructuredText 

Utilities
"""

def crear_lista(cadena):
    l = cadena.splitlines()
    for elem in l:
        if elem == '':
            l.remove(elem)
    return(l)

#Crea lista________________________________________________________________________________
lista = crear_lista(cadena)

#Creamos diccionario con las categorias y la cantidad TOTAL de subcategorias______________ 
dicci = {}
cant = 0
for categoria in lista: 
    if not categoria.startswith('    ') and not categoria.startswith('        '):
        titulo = categoria
        if lista.index(categoria) + 1 < len(lista):
            if lista[lista.index(categoria) + 1].startswith('    ') or lista[lista.index(categoria) + 1].startswith('        '):
                cant = 0
    if categoria.startswith('    ') or categoria.startswith('        '): 
        cant += 1    
    dicci[titulo] = cant
print(dicci)
    
#Listas con categoria, sub cate y subsub cate
#subcategorias = [elem for elem in lista if elem.startswith('    ')]
#subsubcategorias = [elem for elem in lista if elem.startswith('        ')]
#categorias = [elem for elem in lista if elem not in subcategorias and elem not in subsubcategorias and elem != '']





# In[6]:


#12 :c
    
[
'-*-*-',
'--*--',
'----*',
'*----',
]


# In[ ]:




