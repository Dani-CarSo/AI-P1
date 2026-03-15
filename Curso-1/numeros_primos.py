#LAB Modulo 4- Sección 3
# Números primos
# Python essentials 1

def es_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

for i in range(1, 20):
    if es_primo(i +1):
        print(i + 1, end="")
        
print("\n")