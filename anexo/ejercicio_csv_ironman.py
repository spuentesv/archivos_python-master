#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

# Importa libreria
import os    # os
import csv   # csv

# Define listas y diccionarios
catlst = []


def segundos(tiempo):
    # Extrae hh; mm; ss
    slice1 = slice(0,2)
    slice2 = slice(3,5)
    slice3 = slice(6,8)
    hora = int(tiempo[slice1])
    minuto = int(tiempo[slice2])
    segundo = int(tiempo[slice3])

    # transforma hh:mm:ss a ss
    total = ((hora * 3600) + (minuto * 60)) + segundo  
    #print('Hora', hora, 'Minuto', minuto, 'Segundo', segundo, 'Total Segundos', total)
    return total


def tiempo_hhmmss(total_segundos):
    # print total_segundos
    #print('Total Segundos', total_segundos)
    # Convierte segundos a hh:mm:ss
    horas = int(total_segundos) // 3600
    minutos = (int(total_segundos) % 3600) // 60
    segundos = (int(total_segundos) % 60) 
    #print('Horas', horas, 'Minutos', minutos, 'segundos', segundos)
    slice1 = slice(0,2)
    slice2 = slice(1,3)
    hh = '0' + str(horas)
    mm = '0' + str(minutos)
    ss = '0' + str(segundos)
    dato = ''
    # Edita hh:mm:ss
    if len(hh) > 2:
        dato = dato + hh[slice2]
    else:
        dato = dato + hh[slice1]    
    
    if len(mm) > 2:
        dato = dato + ':' + mm[slice2]
    else:
        dato = dato + ':' + mm[slice1]    
    
    if len(ss) > 2:
        dato = dato + ':' + ss[slice2]
    else:
        dato = dato + ':' + ss[slice1]    
    return dato


# Defime funcion de impresion
# List Especialidad, List Nombres, Division, Especialidad
def imprime(divlst, nomlst, pailst, divisionx, especialidad):
    maximo = max(divlst)     
    minimo = min(divlst)
    promedio = sum(divlst)/len(divlst)
    posicion_max = divlst.index(maximo)
    posicion_min = divlst.index(minimo)

    hhmmss_max = tiempo_hhmmss(maximo)
    hhmmss_min = tiempo_hhmmss(minimo)
    print('Division ', especialidad, divisionx, 'Maximo seg', maximo, 'hh:mm:ss', hhmmss_max, 'Corredor', nomlst[posicion_max], 'Pais', pailst[posicion_max])
    print('Division ', especialidad, divisionx, 'Minimo seg', minimo, 'hh:mm:ss', hhmmss_min, 'Corredor', nomlst[posicion_min], 'Pais', pailst[posicion_min]) 
    print('Division ', especialidad, divisionx, 'Minimo seg', promedio)   
    print(' ') 



def ironman(catlst):
    print("Ahora sí! buena suerte :)")

 
    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''
   # Recupera Lista de parametros
    sexdiv = catlst[0]
    division1 = (sexdiv + catlst[1]).strip()
    division2 = (sexdiv + catlst[2]).strip()
    division3 = (sexdiv + catlst[3]).strip()
    division4 = (sexdiv + catlst[4]).strip()
    print('Divisio1', division1, 'Division2', division2, 'Division3', division3, 'Division4', division4)

    # Define Diccionario
    # irolst = {"Division": 4,
    #           "Swim": 5,
    #           "Bike": 6,  
    #           "Run": 7,  
    #           "Name": 1,
    #           "Country": 2
    # }
    irolst1 = {}    # Division 1
    irolst2 = {}    # Division 2
    irolst3 = {}    # DIvision 3
    irolst4 = {}    # Division 4

    # Division 1
    div1slst = []   # swim
    div1blst = []   # bike
    div1rlst = []   # run
    div1plst = []   # posicion
    div1dlst = []   # diccionario
    div1clst = []   # Pais

    # Division 2
    div2slst = []   # swim
    div2blst = []   # bike
    div2rlst = []   # run
    div2plst = []   # posicion
    div2dlst = []   # diccionario
    div2clst = []   # Pais

    # Division 3
    div3slst = []   # swim
    div3blst = []   # bike
    div3rlst = []   # run
    div3plst = []   # posicion
    div3dlst = []   # diccionario
    div3clst = []   # Pais

    # Division 4
    div4slst = []   # swim
    div4blst = []   # bike
    div4rlst = []   # run
    div4plst = []   # posicion
    div4dlst = []   # diccionario
    div4clst = []   # Pais 

    # punteros
    posicion1 = 0
    posicion2 = 0
    posicion3 = 0
    posicion4 = 0

    # Recupera directorio
    dircsv = os.getcwd()
    #print('Directorio csv', dircsv)
    filcsv = dircsv + '/archive/2019 Ironman World Championship Results.csv'
    #print('Archivo csv', filcsv)

    # Define y anexa archivo csv a lista
    csvfile = open(filcsv)
    data = list(csv.DictReader(csvfile))

    # Define diccionario de trabajo
    dic = {}
    totdiv = 0
    # Leer lista 
    for x in data:
        dic.clear()
        #print(x)
       
        # Carga Diccionario irolst1, irolst2, irolst3, irolst4
        dic = x
        categoria = dic.get('Division')
        if (division1 == categoria) or (division2 == categoria) or (division3 == categoria) or (division4 == categoria):
            #print('Division', dic.get('Division'))
            totdiv += 1

        if (division1 == categoria) or (division2 == categoria) or (division3 == categoria) or (division4 == categoria):
            if (len(dic.get('Swim')) > 0) and (len(dic.get('Bike')) > 0) and (len(dic.get('Run')) > 0):
                # Tiempo Swim
                # Convierte hh:mm:ss a ss
                tiempo = dic.get('Swim')
                total_swim = segundos(tiempo)

                # Tiempo Bike
                # Convierte hh:mm:ss a ss
                tiempo = dic.get('Bike')
                total_bike = segundos(tiempo)

                # Tiempo Run
                # Convierte hh:mm:ss a ss
                tiempo = dic.get('Run')
                total_run = segundos(tiempo)            

                #print('Diccionario temporal', dic)
                cargo = False
                if (division1 == dic.get('Division')):
                    try:
                        irolst1['Division'] = dic.get('Division')
                        irolst1['Swim'] = dic.get('Swim')
                        irolst1['Bike'] = dic.get('Bike')
                        irolst1['Run'] = dic.get('Run')
                        irolst1['Name'] = dic.get('Name')
                        irolst1['Country'] = dic.get('Country')
                        div1slst.append(total_swim)
                        div1blst.append(total_bike)
                        div1rlst.append(total_run)
                        div1plst.append(posicion1)
                        div1dlst.append(dic.get('Name'))
                        div1clst.append(dic.get('Country'))
                        posicion1 += 1
                        cargo = True
                        #print('Division1: ',irolst1)
                    except:
                        print('Error en datos division', division1)

                if  (division2 == dic.get('Division')):
                    try:
                        irolst2['Division'] = dic.get('Division')
                        irolst2['Swim'] = dic.get('Swim')
                        irolst2['Bike'] = dic.get('Bike')
                        irolst2['Run'] = dic.get('Run')
                        irolst2['Name'] = dic.get('Name')
                        irolst2['Country'] = dic.get('Country')
                        div2slst.append(total_swim)
                        div2blst.append(total_bike)
                        div2rlst.append(total_run)
                        div2plst.append(posicion2)
                        div2dlst.append(dic.get('Name')) 
                        div2clst.append(dic.get('Country'))                   
                        posicion2 += 1 
                        cargo = True
                        #print('Division2: ',irolst2)   
                    except:
                        print('Error en datos division', division2)

                if  (division3 == dic.get('Division')):
                    try:
                        irolst3['Division'] = dic.get('Division')
                        irolst3['Swim'] = dic.get('Swim')
                        irolst3['Bike'] = dic.get('Bike')
                        irolst3['Run'] = dic.get('Run')
                        irolst3['Name'] = dic.get('Name')
                        irolst3['Country'] = dic.get('Country')
                        div3slst.append(total_swim)
                        div3blst.append(total_bike)
                        div3rlst.append(total_run)
                        div3plst.append(posicion3)
                        div3dlst.append(dic.get('Name'))    
                        div3clst.append(dic.get('Country'))                   
                        posicion3 += 1  
                        cargo = True
                        #print('Division3: ',irolst3) 
                    except:
                        print('Error en datos division', division3)

                if  (division4 == dic.get('Division')):
                    try:
                        irolst4['Division'] = dic.get('Division')
                        irolst4['Swim'] = dic.get('Swim')
                        irolst4['Bike'] = dic.get('Bike')
                        irolst4['Run'] = dic.get('Run')
                        irolst4['Name'] = dic.get('Name')
                        irolst4['Country'] = dic.get('Country')
                        div4slst.append(total_swim)
                        div4blst.append(total_bike)
                        div4rlst.append(total_run)
                        div4plst.append(posicion4) 
                        div4dlst.append(dic.get('Name'))   
                        div4clst.append(dic.get('Country'))                    
                        posicion4 += 1 
                        #print('Division4: ',irolst4)
                    except:
                        print('Error en datos division', division4)

            #if (cargo == False):
            #    print('Diccionario temporal', dic)

    # Imprime lineas procesadas
    print('Lineas procesadas:', totdiv)

    # Determina maximo y minimo
    if (len(div1plst) > 0):             # Division 1
        # Swim
        imprime(div1slst, div1dlst, div1clst, division1, 'Swim')
        
        # Bike
        imprime(div1blst, div1dlst, div1clst, division1, 'Bike')

        # Run
        imprime(div1rlst, div1dlst, div1clst, division1, 'Run')

    if (len(div2plst) > 0):             # Division 2
        # Swim
        imprime(div2slst, div2dlst, div2clst, division2, 'Swim')
        
        # Bike
        imprime(div2blst, div2dlst, div2clst, division2, 'Bike')

        # Run
        imprime(div2rlst, div2dlst, div2clst, division2, 'Run')        
 

    if (len(div3plst) > 0):             # Division 3
        # Swim
        imprime(div3slst, div3dlst, div3clst, division3, 'Swim')
        
        # Bike
        imprime(div3blst, div3dlst, div3clst, division3, 'Bike')

        # Run
        imprime(div3rlst, div3dlst, div3clst, division3, 'Run')        


    if (len(div4plst) > 0):             # Division 4
        # Swim
        # Swim
        imprime(div4slst, div4dlst, div4clst, division4, 'Swim')
        
        # Bike
        imprime(div4blst, div4dlst, div4clst, division4, 'Bike')

        # Run
        imprime(div4rlst, div4dlst, div4clst, division4, 'Run')      



if __name__ == '__main__':
    print("Ejercicios de práctica extra")

    # Define lista categoria (Sexo, Division1, Division2, Division3)
    catlst = ['M','PRO','18-24','25-29','45-49']
    ironman(catlst)
