import random
import time
import csv
import os




trabajadores = ["Juan Perez","Marla Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]

trabajadores_lista = []
def menu_opciones(p_opcs):
    while True:
        print('\tMenu Analisis de trabajadores\n\t1. Asignar sueldos aleatorios\n\t2. Clasificar sueldos\n\t3. Ver estadisticas\n\t4. Reporte de sueldos\n\t5. Salir del programa\n')
        try:
            opc = int(input('Ingrese una opcion: '))
            if opc in p_opcs:
                return  opc
            else:
                print('ERROR! debe ingresar una opcion valida, opciones validas(1,2,3,4,5)!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un numero entero!')

def asignar_sueldos_aleatorios():
    print('Asignar sueldos aleatorios!')
    limpiar_esperar_screen()
    if len(trabajadores_lista) == 0:
        sueldo1_ = random.randint(300000,2500000)
        sueldo2 = random.randint(300000,2500000)
        sueldo3 =random.randint(300000,2500000)
        sueldo4 = random.randint(300000,2500000)
        sueldo5 = random.randint(300000,2500000)
        sueldo6 = random.randint(300000,2500000)
        sueldo7 = random.randint(300000,2500000)
        sueldo8 = random.randint(300000,2500000)
        sueldo9 = random.randint(300000,2500000)
        sueldo10 = random.randint(300000,2500000)

        for i in range(10):
            if i == 0:
                lista = [trabajadores[i],sueldo1_]
                trabajadores_lista.append(lista)
            elif i == 1:
                lista = [trabajadores[i],sueldo2]
                trabajadores_lista.append(lista)
            elif i == 2:
                lista = [trabajadores[i],sueldo3]
                trabajadores_lista.append(lista)
            elif i == 3:
                lista = [trabajadores[i],sueldo4]
                trabajadores_lista.append(lista)
            elif i == 4:
              lista = [trabajadores[i],sueldo5]
              trabajadores_lista.append(lista)
            elif i == 5:
              lista = [trabajadores[i],sueldo6]
              trabajadores_lista.append(lista)
            elif i == 6:
              lista = [trabajadores[i],sueldo7]
              trabajadores_lista.append(lista)
            elif i == 7:
              lista = [trabajadores[i],sueldo8]
              trabajadores_lista.append(lista)
            elif i == 8:
              lista = [trabajadores[i],sueldo9]
              trabajadores_lista.append(lista)
            elif i == 9:
              lista = [trabajadores[i],sueldo10]
              trabajadores_lista.append(lista)
        print(trabajadores_lista)
        time.sleep(2)
    else:
        print('Solo se puede asignar una vez los sueldos aleatorios!')
        limpiar_esperar_screen()
    


def clasificar_sueldos():
    print('Clasificar sueldos!')
    limpiar_esperar_screen()

    if len(trabajadores_lista) >= 1:
        cont_menor_800 = 0
        cont_800_2m = 0
        cont_sup_2m = 0
        sueldos_menores_800 = []
        sueldo_800_2m = []
        sueldo_sup_2m = []
        while True:
            for x in range(10):
                if trabajadores_lista[x][1] <= 800000:
                    sueldos_menores_800.append(trabajadores_lista[x])
                    cont_menor_800 = cont_menor_800 + 1
                elif trabajadores_lista[x][1] >= 800000 and trabajadores_lista[x][1] <= 2000000:
                    sueldo_800_2m.append(trabajadores_lista[x])
                    cont_800_2m = cont_800_2m + 1
                else:
                    sueldo_sup_2m.append(trabajadores_lista[x])
                    cont_sup_2m = cont_sup_2m + 1
            break

        totales_sueldo = 0
        for x in range(10):
            for e in range(1,2):
                if trabajadores_lista[x][e]:
                    totales_sueldo = totales_sueldo + trabajadores_lista[x][e]

        print(f'\tSueldos Menores a $800.000 TOTAL: {cont_menor_800}\n')
        for i in range(cont_menor_800):
            print(f'\tNombre empleado: {sueldos_menores_800[i][0]}\tSueldo ${sueldos_menores_800[i][1]}\n')
        print()
        print(f'\tSueldos entre $800.000 y $2.000.000 TOTAL: {cont_800_2m}\n')
        for e in range(cont_800_2m):
            print(f'\tNombre empleado: {sueldo_800_2m[e][0]}\tSueldo ${sueldo_800_2m[e][1]}\n')
        print()
        print(f'\tSueldos superiores a 2.000.000 TOTAL: {cont_sup_2m}\n')
        for a in range(cont_sup_2m):
              print(f'\tNombre empleado: {sueldo_sup_2m[a][0]}\tSueldo ${sueldo_sup_2m[a][1]}\n')
        print()
        print(f'TOTAL SUELDOS: ${totales_sueldo}')
        time.sleep(5)
        limpiar_esperar_screen()
    else:
        print('NO HAY SUELDOS REGISTRADOS AUN!')
    limpiar_esperar_screen()
    

def estadisticas():
    print('Ver estadisticas!')
    limpiar_esperar_screen()

    if len(trabajadores_lista) >= 1:
        mayor_sueldo = 0
        for x in range(10):
            if trabajadores_lista[x][1] > mayor_sueldo:
                mayor_sueldo = trabajadores_lista[x][1]
            
        menor_sueldo = trabajadores_lista[0][1]
        for n in range(10):
            if menor_sueldo > trabajadores_lista[n][1]:
                menor_sueldo =  trabajadores_lista[n][1]

        lista_sueldos = []
        for t in range(10):
            if trabajadores_lista[t][1]:
                lista_sueldos.append(trabajadores_lista[t][1])
        
        promedio = int((lista_sueldos[0]+lista_sueldos[1]+lista_sueldos[2]+lista_sueldos[3]+lista_sueldos[4]+lista_sueldos[5]+lista_sueldos[6]+lista_sueldos[7]+lista_sueldos[8]+lista_sueldos[9]) / 10)

        m_g = int((lista_sueldos[0] * lista_sueldos[1]* lista_sueldos[2]* lista_sueldos[3]*lista_sueldos[4] * lista_sueldos[5]* lista_sueldos[6]* lista_sueldos[7]*lista_sueldos[8]*lista_sueldos[9]) ** (1/10))
        
        while True:
            print(f'\tEstadisticas de sueldo\n\tSueldo mas alto: {mayor_sueldo}\n\tSueldo mas bajo: {menor_sueldo}\n\tPromedio de sueldos: {promedio}\n\tMedia Geometrica: {m_g}')
            mensaje_salida = str(input('¿Deseas salir? Ingrese ("S":salir "N":redirigir estadisticas): '))
            if mensaje_salida.upper() in ("S","N"):
                if mensaje_salida.upper() == "S":
                    print('Saliendo.')
                    limpiar_esperar_screen()
                    break
                else:
                    print('Redirigiendo.')
                limpiar_esperar_screen()
            else:
                print('ERROR! debe ingresar una opcion valida, opciones validas("S" o "N")!')
            limpiar_esperar_screen()
    else:
        print('NO HAY SUELDOS REGISTRADOS!')
    limpiar_esperar_screen()

def reporte_sueldos():
    print('Reporte de sueldos!')
    limpiar_esperar_screen()

    if len(trabajadores_lista) >= 1:
        for i in range(10):
            if trabajadores_lista[i][1]:
                sueldo_base = trabajadores_lista[i][1]
                desc_salud = int(sueldo_base * 0.07) 
                desc_afp = int(sueldo_base * 0.12)
                sueldo_liq = int(sueldo_base - (desc_afp + desc_salud))
                trabajadores_lista[i].append(desc_salud)
                trabajadores_lista[i].append(desc_afp)
                trabajadores_lista[i].append(sueldo_liq)
        

        while True:
            nombre_archivo = str(input('Ingrese el nombre del archivo: '))
            if len(nombre_archivo.strip()) >= 3:
                print('Nombre archivo registado!')
                limpiar_esperar_screen()
                break
            else:
                print('ERROR! debe ingresar un nombre que contenga al menos 3 caracteres!')
            limpiar_esperar_screen()

        
        try: 
            with open(f"{nombre_archivo}.csv","x",newline="") as archivo:
                escritor = csv.writer(archivo)
                titulos = ["Nombre empleado","Sueldo base","Descuento Salud", "Descuento AFP","Sueldo liquido"]
                escritor.writerow(titulos)
                
                print(titulos)
                for x in trabajadores_lista:
                    print(x)
                escritor.writerows(trabajadores_lista)
            print('ARCHIVO CREADO!')
            limpiar_esperar_screen()
            return 
        except:
            print('ERROR EL NOMBRE DEL ARCHIVO YA EXISTE!')                    



            
        



    
        




    

def limpiar_esperar_screen():
    time.sleep(1)
    os.system('cls')


def salir():
    for x in range(1,4):
        print('Finalizando programa',("."*x))
        limpiar_esperar_screen()
    print('Desarrollado por César Flores\n\tRUT 20.834.489-7')
    limpiar_esperar_screen()





    # for i in trabajadores:
    #     if i == trabajadores[0]:
    #         trabajadores[0].append(aleatorio)
    #     else:
    #         trabajadores.append(aleatorio)
