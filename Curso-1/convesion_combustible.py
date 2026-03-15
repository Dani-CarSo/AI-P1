#LAB Modulo 4- Sección 3
# Conversión de combustible 
# Python essentials 1

def litros_100km_a_millas_galon(litros):
    millas = 100000 / 1609.34
    galones = litros / 3.78541
    return millas / galones

def millas_galon_a_litros_100km(millas):
    litros=3.78541
    km=millas * 1609.34 
    return litros / (km / 100)

print(litros_100km_a_millas_galon(3.9))
print(litros_100km_a_millas_galon(7.5))
print(litros_100km_a_millas_galon(10.0))    
print(millas_galon_a_litros_100km(60.3))
print(millas_galon_a_litros_100km(31.4))
print(millas_galon_a_litros_100km(23.5))