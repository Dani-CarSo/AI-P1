#LAB Modulo 3- Sección 2
#Bucles en python
# Python essentials 1

import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("Fin")

palabra_secreta="chupacabra"
while True:
    palabra=input("¿Cuál es la palabra secreta? ")
    if palabra == palabra_secreta:
        print("¡Has adivinado la palabra secreta!")
        break
    else:
        print("¡Inténtalo de nuevo!")
        
        
        
user_word=input("Ingresa una palabra: ")
user_word=user_word.upper()
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    print(letter)
    
    
blocks = int(input("Ingresa el número de bloques: "))
height = 0
layer = 1
while blocks >= layer:
    blocks = blocks - layer
    height = height + 1
    layer = layer + 1
print("La altura de la pirámide es:", height)


c0 = int(input("Ingresa un número natural: "))
steps = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1
print("Número de pasos:", steps)

