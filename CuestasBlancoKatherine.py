import csv
estudiantes = [] 
estudiantes={}
def mostrar_menu():#forma de definir una función
  
  while True: 
    print("****Bievenido al sistema del colegio “EducandoAndo****”")
    print("1. Procesar lista de estudiantes")
    print("2. Registrar estudiante.")
    print("3. Modificar nota")
    print("4. Eliminar estudiante")
    print("4. Generar promedio de notas")
    print("3. Generar acta de cierre de curso")
    print("4. Salir")
    try:      
      opcion = int(input("Ingrese su opción: "))
      if opcion < 1 or opcion > 6:
        print("Ingrese una opción válida! (1-6)")
      else:
        return opcion
    except ValueError:
      print("Ingrese una opción válida! (1-6)")

def procesar_lista_estudiantes(rut,nombre_apellido,nota1,nota2):
    
    with open("ListaCurso5B.csv", 'r', ) as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            rut = fila["Rut"]
            nombre_apellido = fila["Nombre"]
            nota1 = float[fila["Nota 1"]]
            nota2 = float[fila["Nota 2"]]

            estudiante = {
                "rut": rut,
                "nombre": nombre_apellido,
                "nota1": nota1,
                "nota2": nota2,               
            }            
            estudiantes.append(estudiante)
    print("Estudiantes cargados exitosamente.")
    return estudiantes

def registrar_estudiante(rut,nombre_apellido,nota1,nota2): 
    while True:
        rut = input("Ingrese el rut: ")
        if len(rut) == 0: 
            print("Ingrese un nombre válido!")
        else:
            break 
    while True:
        nombre_apellido = input("Ingrese el nombre y apellido ")
        if len(nombre_apellido) == 0:
            print("Ingrese un apellido válido!")
        else:
                break
    while True:
        nota1 = input("Ingrese la nota 1 : ")
        if len(nota1) == 0:
            print("Ingrese una nota")
        else:
                break
    while True:
        nota2 = input("Ingrese la nota 2: ")
        if len(nota2) == 0:
            print("Ingrese la nota 2")
        else:
                break
    nuevo_estudiante = { 
        "RUT" : rut,
        "Nombre y Apellido" : nombre_apellido,
        "Nota 1" : nota1,
        "Nota 2" : nota2,
    }
    estudiantes.append(nuevo_estudiante)
    
def modificar_nota():
    rut = input("Ingrese el rut a modificar: ")
    for estudiante in estudiantes:
        if estudiante["RUT"] == rut:
            estudiante["Nombre y Apellido"] = input("Ingresa el nombre y apellido")
            estudiante["Nota 1"] = input("NOTA 1 ")
            estudiante["Nota 2"] = input("NOTA 2")
def eliminar_estudiante():
    print("Hola eliminar estudiante")
def genear_promedio_notas():
    print("Hola generar promedio de notas")
def generar_acta_cierre_curso():
    print("Hola generar acta de cierre")
    
def main():
        
    while True:
        opcion = mostrar_menu()
        if opcion == 1:   
            rut=input("Ingresa tu rut: ")
            nombre_apellido=input("Ingresa tu nombre y apellido: ")
            nota1=float(input("Ingresa la nota 1: "))
            nota2=float(input("Ingresa la nota 2: "))
            estudiantes = procesar_lista_estudiantes(rut,nombre_apellido,nota1,nota2)     
        elif opcion == 2:
            estudiantes=registrar_estudiante(rut,nombre_apellido,nota1,nota2)
        elif opcion == 3:
            modificar_nota()
        elif opcion == 4:
            eliminar_estudiante()
        elif opcion == 5:
            genear_promedio_notas()
        elif opcion == 6:
            generar_acta_cierre_curso
        elif opcion == 7:
            print("Adios!")
        break
    input("Presione Enter para continuar...")  


main()
