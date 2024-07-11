from funciones import *

print('Bievenido a la app de analisis de datos trabajadores!')
limpiar_esperar_screen()
opciones = (1,2,3,4,5)

while True:
    limpiar_esperar_screen()
    opc = menu_opciones((opciones))
    if opc == 1:
        asignar_sueldos_aleatorios()
    elif opc == 2:
        clasificar_sueldos()
    elif opc == 3:
        estadisticas()
    elif opc == 4:
        reporte_sueldos()
    else:
        salir()
        break