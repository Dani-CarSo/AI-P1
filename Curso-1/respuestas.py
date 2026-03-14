#LAB Modulo 3- Sección 1
# Variables- Preguntas y respuestas, operadores y setencia de if-else
# Python essentials 1

print("Preguntas y respuestas")

n=int(input("¿Cuántos años tienes? "))
if n >= 18:
    print("Eres mayor de edad") 
else:
    print("Eres menor de edad")

name=input("¿Cuál es tu nombre? ")
if name == "Harry":
    print("Hola Harry, bienvenido a Hogwarts")
elif name == "Hermione":
    print("Hola Hermione, bienvenido a Hogwarts")
elif name == "Ron":
    print("Hola Ron, bienvenido a Hogwarts")
else:
    print("Hola " + name + ", bienvenido a Hogwarts")
    
intro=input("¿Cuál es tu materia favorita? ")
if intro == "Pociones":         
    print("¡Excelente elección! Las pociones son fascinantes.")
elif intro == "Defensa contra las artes oscuras":
    print("¡Genial! La defensa contra las artes oscuras es una materia muy importante.")
elif intro == "Transformaciones":
    print("¡Interesante! Las transformaciones son una materia desafiante pero gratificante.")
else:
    print("¡Buena elección! " + intro + " es una materia muy interesante.")
    