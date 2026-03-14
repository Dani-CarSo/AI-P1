#LAB Modulo 2- Sección 4
# Variables Convertidor simple y operadores y expresiones
# Python essentials 1

print("Variables:Convertidor simple")

# Convertidor de pulgadas a centímetros
pulgadas = 10
centimetros = 25.4

pulgadas_a_centimetros = pulgadas * centimetros
centimetros_a_pulgadas = pulgadas_a_centimetros / centimetros

print(pulgadas, "pulgadas son", pulgadas_a_centimetros, "centímetros")
print(pulgadas_a_centimetros, "centímetros son", centimetros_a_pulgadas, "pulgadas")


print("Operadores y expresiones")
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
