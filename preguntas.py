"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0         #inicializa la variable suma
    with open('data.csv', 'r') as f:
        for linea in f:
            valores = linea.strip().split('\t') #Utiliza tabulador como separador del archivo csv
            try:
                suma = suma + int(valores[1])
            except (ValueError, IndexError):
                pass 
    return suma
print(pregunta_01())        


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    conteo = {} #diccionario para almacenar el conteo de cada letra
    with open('data.csv', 'r') as f:
        for linea in f:
            letra = linea.strip().split()[0] #Obtener la primera letra de cada línea
            conteo[letra] = conteo.get(letra,0)+1 #Incrementar el conteo de la letra
    lista_tuplas = sorted(conteo.items()) #Convertir el diccionario en una lista de tuplas y ordenarlo
    return lista_tuplas
print(pregunta_02())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    
    """
    suma_por_letra = {} # Diccionario para almacenar la suma de la columna 2 para cada letra de la columna 1
    with open('data.csv', 'r') as f: # Abre el archivo data.csv en modo lectura
        for linea in f: # Itera sobre cada línea del archivo
            valores = linea.strip().split() # Divide en valores
            letra = valores[0] # Obtiene la letra de la primera columna
            numero = int(valores[1]) # Obtiene el número de la segunda columna
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + numero # Incrementa la suma de la letra
    resultado = sorted(suma_por_letra.items()) # Convierte el diccionario en una lista de tuplas y las ordena
    return resultado
print(pregunta_03()) # Llama a la función e imprime el resultado



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    conteo_por_mes = {} # Diccionario para almacenar el conteo de registros de cada uno de los meses
    with open('data.csv', 'r') as f: # Abre el archivo data.csv en modo lectura
        for linea in f: # Itera sobre cada una de las líneas del archivo
            valores = linea.strip().split() # Divide la línea en valores
            fecha = valores[2] # Obtiene la fecha de la 3ra ccolumna
            mes = fecha.split('-')[1] # Extrae el mes de la fecha (parte de la cadena despues del segundo guion)
            if mes in conteo_por_mes: # Verifica si el mes ya está en el diccionario
                conteo_por_mes[mes] += 1 #si está en el diccionario, incrementa el conteo
            else:
                conteo_por_mes[mes] = 1 # Si no está en el diccionario, crea una nueva entrada con conteo 1
    resultado = sorted(conteo_por_mes.items()) # Convierte el diccionario en una lista de tuplas y la ordena
    return resultado
print(pregunta_04()) # Llama a la función e imprime el resultado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    valores_por_letra = {}
    with open('data.csv', 'r') as f:
        for linea in f:
            valores = linea.strip().split()
            letra = valores[0]
            numero = int(valores[1])
            if letra in valores_por_letra:
                valores_por_letra[letra] = (
                    max(valores_por_letra[letra][0], numero),
                    min(valores_por_letra[letra][1], numero)
                )
            else:
                valores_por_letra[letra] = (numero, numero)
    resultado = sorted([(letra, max_min[0], max_min[1]) for letra, max_min in valores_por_letra.items()])
    return resultado
print(pregunta_05())



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    valores_por_clave = {}
    with open('data.csv', 'r') as f:
        for linea in f:
            valores = linea.strip().split()
            diccionario = valores[4]
            elementos = diccionario.split(',')
            for elemento in elementos:
                clave, valor = elemento.split(':')
                valor = int(valor)
                if clave in valores_por_clave:
                    valores_por_clave[clave].append(valor)
                else:
                    valores_por_clave[clave] = [valor]                 
    resultado = []
    for clave, valores in valores_por_clave.items():
        min_valor = min(valores)
        max_valor = max(valores)
        resultado.append((clave, min_valor, max_valor))

    resultado = sorted(resultado)
    return resultado
print (pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    letras_por_valor={}
    with open('data.csv', 'r') as f:
        for linea in f:
            valores = linea.strip().split()
            valor_columna2 = int(valores[1])
            valor_columna1 = valores[0]
            if valor_columna2 in letras_por_valor:
                letras_por_valor[valor_columna2].append(valor_columna1)
            else:
                letras_por_valor[valor_columna2] =[valor_columna1]
    resultado = sorted(letras_por_valor.items())
    return resultado
print(pregunta_07())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    letras_por_valor={}
    with open('data.csv', 'r') as f:
        for linea in f:
            valores = linea.strip().split()
            valor_columna2 = int(valores[1])
            letra_columna1 = valores[0]
            if valor_columna2 in letras_por_valor:
                letras_por_valor[valor_columna2].append(letra_columna1)
            else:
                letras_por_valor[valor_columna2]=[letra_columna1]
    resultado = [(valor, sorted(set(letras))) for valor, letras in letras_por_valor.items()]
    resultado = sorted(resultado)
    return resultado
print(pregunta_08())


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    registros_por_clave={}
    with open('data.csv', 'r') as f:
        for linea in f:
            valores=linea.strip().split()
            diccionario = valores[4]
            pares_clave_valor = diccionario.split(',')
            for par in pares_clave_valor:
                clave, valor = par.split(':')
                registros_por_clave[clave]=registros_por_clave.get(clave,0) + 1
    registros_por_clave = dict(sorted(registros_por_clave.items()))
    return registros_por_clave
print(pregunta_09())


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    resultados = []
    with open('data.csv', 'r') as f:
        for linea in f:
            valores = linea.strip().split('\t')
            letra_columna_1 = valores[0]
            elementos_columna_4 = len(valores[3].split(','))
            elementos_columna_5 = len(valores[4].split(','))
            resultados.append((letra_columna_1, elementos_columna_4, elementos_columna_5))
    return resultados

print(pregunta_10())



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_letras = {}
    with open('data.csv', 'r') as f:
        for linea in f:
            valores = linea.strip().split()
            letras_columna_4 = valores[3].split(',')
            cantidad = int(valores[1])
            for letra in letras_columna_4:
                suma_letras[letra] = suma_letras.get(letra, 0) + cantidad
    
    # Ordenar el diccionario alfabéticamente por las claves
    suma_letras_ordenadas = dict(sorted(suma_letras.items()))
    return suma_letras_ordenadas

print(pregunta_11())



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    # Inicializamos un diccionario para almacenar la suma de los valores de la columna 5 para cada letra de la columna 1
    suma_por_letra = {}

    # Abrimos el archivo CSV
    with open('data.csv', 'r') as f:
        # Iteramos sobre cada línea del archivo
        for linea in f:
            # Separamos los valores de la línea
            valores = linea.strip().split()
            # Obtenemos la letra de la columna 1
            letra_columna_1 = valores[0]
            # Obtenemos los valores de la columna 5
            valores_columna_5 = valores[4].split(',')
            # Iteramos sobre cada valor de la columna 5
            for valor in valores_columna_5:
                # Dividimos el valor para obtener la clave y el valor asociado
                clave, valor = valor.split(':')
                # Sumamos el valor al diccionario correspondiente a la letra de la columna 1
                suma_por_letra[letra_columna_1] = suma_por_letra.get(letra_columna_1, 0) + int(valor)

    # Ordenamos el diccionario resultante por las claves (letras de la columna 1)
    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))

    return suma_por_letra_ordenada

print(pregunta_12())