# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos
import os
import csv

# Define rutina - valida numeros
def numero(dato):
    valor = True
    try:
        nro = int(dato)
    except:
        valor = False
    return(valor)       
    
def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    # Define varias de trabajo
    articulo = 'tornillos'
    existencia = 0

    # Recupera directorio
    dircsv = os.getcwd()
    #print('Directorio csv', dircsv)
    filcsv = dircsv + '/' + archivo
    #print('Archivo csv', filcsv)

    # Define y anexa archivo csv a lista
    csvfile = open(filcsv, 'r')
    data = list(csv.DictReader(csvfile))  

    # Define diccionario de trabajo
    dic = {}
    # Leer lista 
    for x in data:
        dic.clear()
        #print(x)
       
        # Carga Diccionario temporal 
        dic = x
        #print('tornillos', dic.get('tornillos'))
        
        try:
            unidades = dic.get('tornillos')
        except:
            unidades = 0 

        # Acumula tornillos       
        if (numero(unidades)):
            existencia = existencia + int(unidades)
        else:
            continue

    # Imprime total de existencia de tornillos
    print('Total de ', articulo, existencia)


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

   # Define varias de trabajo
    ambiente2 = 0
    ambiente3 = 0

    # Recupera directorio
    dircsv = os.getcwd()
    #print('Directorio csv', dircsv)
    filcsv = dircsv + '/' + archivo
    #print('Archivo csv', filcsv)

    # Define y anexa archivo csv a lista
    csvfile = open(filcsv, 'r')
    data = list(csv.DictReader(csvfile))  

    # Define diccionario de trabajo
    dic = {}

    # Leer lista 
    for x in data:
        dic.clear()
        #print(x)
       
        # Carga Diccionario temporal 
        dic = x
        #print('Ambientes', dic.get('ambientes'))

        try:
            unidades = dic.get('ambientes')
        except:
            unidades = 0    

        # Acumula deptos de 2 y 3 ambientes    
        if (numero(unidades)):
            if (int(unidades) == 2):
                ambiente2 += 1 
            elif (int(unidades) == 3):  
                ambiente3 += 1 

    # Imprime total de existencia de tornillos
    print('Total depto ', '2 ambientes', ambiente2, '3 ambientes', ambiente3)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
