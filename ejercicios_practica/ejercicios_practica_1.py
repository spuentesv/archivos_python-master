# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con diccionarios
import os
import csv

# Define rutina - valida numeros
def numero(dato):
    valor = True
    try:
        nro = int(dato)
    except:
        print('Error..dato ingresado no es un numero entero') 
        valor = False
    return(valor)       

def ej1():
    print('Ejercicios con diccionarios 1º')
    # Crear un diccionario vacio
    # el diccionario vacio debe llamarse "stock"

     # Recupera directorio
    dircsv = os.getcwd()
    #print('Directorio csv', dircsv)
    filcsv = dircsv + '/stock1.csv'
    #print('Archivo csv', filcsv)

    # Define y anexa archivo csv a lista
    csvfile = open(filcsv, 'w', newline='')

    # Define Header
    header = ['tornillos','tuercas','arandelas'] 

    # Crear archivo csv, basado en cabecera
    writer = csv.DictWriter(csvfile, fieldnames=header) 
    writer.writeheader()

    # stock = ....

    # Luego de crear el diccionario completelo
    # con el siguiente stock:
    # tornillos = 100
    # tuercas = 150
    # arandelas = 300
    
    # Los nombres tornillos, tuercas y arandelas
    # son las claves (keys) del diccionario
    # mientras que las cantidades son los valores (values)
    csvrow = {'tornillos':100, 'tuercas':150, 'arandelas':300}

    # Una vez armado el diccionario imprimirlo en pantalla con print
    print('Archivo cvs',csvrow)

    # Comenzar aquí, recuerde el identado dentro de esta funcion
     # Define row a cargar 
    writer.writerow(csvrow)

     # Cierra csv
    csvfile.close()

def ej2():
    print('Ejercicio con diccionarios 2º')
    # Basado en el ejercicio anterior ej1, utilizaremos el diccionario
    # como una base de datos. Comenzaremos con un diccionario de stock
    # de nuestros productos en cero:
    
    stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}

    # Recupera directorio
    dircsv = os.getcwd()
    #print('Directorio csv', dircsv)
    filcsv = dircsv + '/stock2.csv'
    #print('Archivo csv', filcsv)

    # Define y anexa archivo csv a lista
    csvfile = open(filcsv, 'w', newline='')
 
    # Define Header
    header = ['tornillos','tuercas','arandelas'] 

    # Crear archivo csv, basado en cabecera
    writer = csv.DictWriter(csvfile, fieldnames=header) 
    writer.writeheader()

    # Paso 1:
    # Crear un bucle utilizando while que se ejecute de forma infinita
    # while True.....
    
    # Paso 2:
    # Dentro de ese bucle consultar al usuario por consola
    # que producto desea agregar al stock
    #   - Si el usuario ingresa "FIN" como producto se debe 
    #   finalizar el bucle
    #   - Si el usuario ingresa un producto no definido en el stock
    #   se debe enviar un mensaje de error. (si desea investigar esto
    #   se resuelve muy bien utilizando el operador "in" con diccionarios)

    # Paso 3:
    # Luego de haber ingresado el producto se debe ingresar por consola
    # cuanto stock de ese producto se desea agregar al stock.
    # Si teniamos 20 tornillos y el usuario desea agregar 10 tornillos más,
    # en nuestro diccionario deben quedar 30 tornillos (debe acumular)

    # Paso 4:
    # Cuando el usuario ingrese "FIN" y se termine el bucle, debe
    # imprimir en pantalla con print el diccionario con el stock final

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    termina = False
    while termina == False:
        articulo = input('Ingrese producto (tornillos, tuercas, arandelas o FIN=TERMINAR): \n')
        producto = articulo.lower()
        if (producto == 'fin'):
            termina = True
            break

        if not(producto in stock):
            print('Error..', producto, 'No existe en diccionario STOCK') 
            break

        entero = False    
        while entero == False:    
            unidades = input('ingrese stock (enteros ej. 10, 40, 1): \n')
            if (numero(unidades)):
                entero = True

        # Actualiza stock
        stock[producto] = unidades

    # Define row a cargar 
    writer.writerow(stock)   
    
    # Cierra csv
    csvfile.close()
       
    # Imprime Diccionario Stock
    print('Diccionario Stock', stock)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
