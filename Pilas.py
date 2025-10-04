# SISTEMA DE NOTAS ESCOLAR (versión con pilas, colas y ordenamientos)

def pedir_numero_estudiantes():
    n = 0
    while n <= 0:
        try:
            n = int(input("¿Cuántos estudiantes? "))
            if n <= 0:
                print("Tiene que ser más que 0")
        except:
            print("¡Pon un número válido!")
    return n

def ingresar_datos(n):
    nombres = []
    notas = []
    aprobados = 0
    reprobados = 0

    for i in range(n):
        print(f"\n--- Estudiante {i+1} ---")
        nombre = input("Nombre: ")
        nombres.append(nombre)

        nota_valida = False
        while not nota_valida:
            try:
                nota = float(input("Nota (0-100): "))
                if nota >= 0 and nota <= 100:
                    notas.append(nota)
                    nota_valida = True
                    if nota >= 60:
                        aprobados += 1
                    else:
                        reprobados += 1
                else:
                    print("La nota debe estar entre 0 y 100")
            except:
                print("Eso no es un número")
    return nombres, notas, aprobados, reprobados

def mostrar_resumen(n, aprobados, reprobados):
    print("\n--- RESULTADOS ---")
    print("Total:", n)
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)

def mostrar_todos(nombres, notas):
    print("\n--- TODOS LOS ESTUDIANTES ---")
    for i in range(len(nombres)):
        if notas[i] >= 60:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        print(nombres[i], ":", notas[i], "-", estado)

def calcular_promedio(notas):
    if len(notas) > 0:
        suma = 0
        for nota in notas:
            suma = suma + nota
        promedio = suma / len(notas)
        print("\nPromedio del grupo:", promedio)

#PILA 
def usar_pila(historial):
    print("\n--- PILA (Historial) ---")
    print("Acciones guardadas:", historial)
    if len(historial) > 0:
        ultima = historial.pop()
        print("Se quitó la última acción:", ultima)
        print("Historial ahora:", historial)

#COLA
def usar_cola(nombres):
    print("\n--- COLA (Revisión de estudiantes) ---")
    cola = nombres.copy()
    print("Cola inicial:", cola)
    while len(cola) > 0:
        estudiante = cola.pop(0)
        print("Atendiendo a:", estudiante, " | Cola actual:", cola)

#BURBUJA
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

#INSERCIÓN
def ordenamiento_insercion(lista):
    n = len(lista)
    for i in range(1, n):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = clave
    return lista

def main():
    print("SISTEMA DE NOTAS ESCOLAR")
    print("-----------------------")

    historial = [] 
    n = pedir_numero_estudiantes()
    historial.append("Se pidió número de estudiantes")

    nombres, notas, aprobados, reprobados = ingresar_datos(n)
    historial.append("Se ingresaron datos de los estudiantes")

    mostrar_resumen(n, aprobados, reprobados)
    historial.append("Se mostró el resumen")

    mostrar_todos(nombres, notas)
    historial.append("Se mostraron todos los estudiantes")

    calcular_promedio(notas)
    historial.append("Se calculó el promedio del grupo")

   
    usar_pila(historial)

   
    usar_cola(nombres)

  
    print("\n--- ORDENAMIENTOS ---")
    print("Notas originales:", notas)
    print("Burbuja:", ordenamiento_burbuja(notas.copy()))
    print("Inserción:", ordenamiento_insercion(notas.copy()))



if __name__ == "__main__":
    main()
