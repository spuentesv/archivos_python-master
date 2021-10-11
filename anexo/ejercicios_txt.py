#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"
import os
import csv
import re


def ej1():
    # Ejercicios con archivos txt
    print('Ejercicios con archivos txt # 1')
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    # Recupera directorio
    dirtxt = os.getcwd()
    #print('Directorio txt', dirtxt)
    filtxt = dirtxt + '/notas.txt'
    #print('Archivo txt', filtxt)

    # Lectura de Archivo de Entrada
    with open(filtxt) as fi:
        for line in fi:
            cantidad_lineas += 1

    # Imprime total de linea
    print('Total de lineas', cantidad_lineas)

def ej2():
    # Ejercicios con archivos txt
    print('Ejercicios con archivos txt # 2')
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('nota.txt', 'r')
    # fo = open(.......)

    # Recuerde cerrar los archivos al final ;)

    # Recupera directorio
    dirtxt = os.getcwd()
    #print('Directorio txt', dirtxt)
    filtxt = dirtxt + '/notas.txt'
    #print('Archivo txt', filtxt)

    # Apertura de archivo de salida
    fil1txt = dirtxt + '/notas1.txt'
    fo = open(fil1txt, 'w')

    # Lectura de Archivo de Entrada
    with open(filtxt) as fi:
        for line in fi:
            cantidad_lineas += 1
            fo.write(line)

    # Cierra Archivo de Salida
    fo.close()

    # Imprime total de linea
    print('Total de lineas', cantidad_lineas)

def ej3():
    print("Cuenta caracteres")
    print('Ejercicios con archivos txt # 3')    
    cantidad_letras = 0

    '''
    Realizar un programa que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    # Recupera directorio
    dirtxt = os.getcwd()
    #print('Directorio txt', dirtxt)
    filtxt = dirtxt + '/texto.txt'
    #print('Archivo txt', filtxt)

    # Lectura de Archivo de Entrada
    with open(filtxt) as fi:
        for line in fi:
            cantidad_letras = cantidad_letras + len(line)

    # Imprime total de linea
    print('Total de letras', cantidad_letras)

def ej4():
    print("Transcribir!")
    print('Ejercicios con archivos txt # 4')    
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    # Recupera directorio
    dirtxt = os.getcwd()
    #print('Directorio txt', dirtxt)
    filtxt = dirtxt + '/notas.txt'
    #print('Archivo txt', filtxt)

    # Apertura de archivo de salida
    filtxt = dirtxt + '/texto1.txt'
    fo = open(filtxt, 'w')  

    termina = False
    while termina == False:
        linea = input('Ingrese texto (texto vacio = finaliza): ')

        # SI, ingreso dato lo graba en Archivo de Salida
        if (len(linea) > 0):
            fo.write(linea + '\n') 
        else: break         

    # Cierre Archivo de Salida
    fo.close()  


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
