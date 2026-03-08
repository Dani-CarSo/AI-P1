#Modulo 1- Sección 2
#Introducción a Python
#Python essentials 1

print("Bienvenido a Python Essentials 1")
print("En este programa aprenderas la historia de Python")
print("ASI QUE EMPECEMOS.....")

def que_es_python():
    print(" Es un lenguaje de programación de alto nivel, interpretado, orientado a objetos, con semantica dinamica  y de propósito general.")
  
def creador_de_python():
    print("Python fue creado por Guido van Rossum y su primera versión fue lanzada en 1991.") 

def datos_curiosos():
    print("Datos curiosos acerca del programa")
    print("1. El nombre de Python no proviene de la serpiente, sino del programa de televisión británico 'Monty Python's Flying Circus'.")
    print("2.Python fue creado como un proyecto de hobby durante la semana de  Navidad, ")
    print("3.Guido usó el lenguaje de programación 'C' para implementar la primera versión de su lenguaje y esta decisión aún está vigente.")
    print("4. Es uno de los lenguajes de programación más populares y utilizados en el mundo, con una gran comunidad de desarrolladores y una amplia variedad de aplicaciones, desde desarrollo web hasta inteligencia artificial.")  

def sus_objetivos():
    print("Los objetivos de Python son:")
    print("1. Ser fácil de aprender y usar")
    print("2. Ser un lenguaje de codigo abierto, para que cualquiera pueda contribuir a su desarrollo   ")
    print("3. Fomentar la legibilidad del código")
    print("4. Permitir la programación orientada a objetos, funcional y procedimental")
  
def implementaciones():
    print("Existen varias implementaciones de Python, cada una con sus propias características y usos. Algunas de las implementaciones más populares incluyen:")
    print("1. CPython: Escrita en C. Es la más utilizada y compatible con la mayoría de las bibliotecas y herramientas de Python.")
    print("2. Jython: Escrita en Java, que permite ejecutar código Python en la máquina virtual de Java (JVM).")
    print("3. MicroPython: Es diseñada para microcontroladores y sistemas embebidos, con un enfoque en la eficiencia y el bajo consumo de recursos.")
    print("4. PyPy: Escrita en RPython, que se centra en mejorar el rendimiento mediante técnicas como la compilación Just-In-Time (JIT).")

def rivales():
    print("Pearl")
    print("Ruby")
    print("¿Quieres saber mas acerca de estos rivales?")
    
    respuesta = input("Escribe 'Si' o 'No': ")
    
    if respuesta() == 'Si':
        print("Traidor, apoya a Python, no a sus rivales")
   
    if respuesta() == 'No':
     print(" Que fiel eres, me gusta tu lealtad a Python")

def conclusion():  
    print( "Python es facil de aprender, enseñar, facil de utilizar, entender y de instalar")
    
def menu():
    while True:
     print("¿Que te gustaria aprender hoy?")
     print("1. Que es Python")
     print("2. Quien creo Python")
     print("3. Datos curiosos acerca de Python")
     print("4. Cuales son los objetivos de Python")
     print("5. Cuales son las implementaciones de Python")
     print("6. Quienes son los rivales de Python")
     print("7. Conclusion")
    
    opcion= input("Seleccione la opcion que deseas.")
    if opcion == '1':
            que_es_python()
    elif opcion == '2':
            creador_de_python()
    elif opcion == '3':
            datos_curiosos()
    elif opcion == '4':
            sus_objetivos()
    elif opcion == '5':
            implementaciones()
    elif opcion == '6':
            rivales()
    elif opcion == '7':
            conclusion()
    else:
            print("Opcion no valida, por favor seleccione una opcion del 1 al 7.")

menu()