#LAB Modulo 3- Sección 4 y 6
# Listas y Operaciones con listas
# Python essentials 1

print("The beatles")

beatles=[]
print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")        
beatles.append("George Harrison")
print("Paso 2:", beatles)

for i in range(2):
    miembro = input("Ingrese el nombre de un miembro de los Beatles: ")
    beatles.append(miembro)
print("Paso 3:", beatles)

del beatles[3]
del beatles[3]
print("Paso 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

print("Operaciones con listas:")
my_list=[1,2,4,4,1,4,2,6,2,9]

unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
        
print("Lista original:", my_list)
print("Lista con elementos únicos:", unique_list)