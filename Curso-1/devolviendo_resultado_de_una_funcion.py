# Modulo 4- Sección 3
# Un año bisiesto
# Python essentials 1

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_resultados = [False, True, True, False]

for i in range(len(test_data)):
    anio = test_data[i]
    resultado = es_bisiesto(anio)
    print(anio, "->", end=" ")
    if resultado == test_resultados[i]:
        print("OK")
    else:
        print("Fallido")


def dias_en_mes(anio, mes):
    if anio < 1 or mes < 1 or mes > 12:
        return None

    dias = [31,28,31,30,31,30,31,31,30,31,30,31]

    if mes == 2 and es_bisiesto(anio):
        return 29

    return dias[mes-1]


test_anios = [1900, 2000, 2016, 1987, 2024, 2023, -5]
test_meses = [2, 2, 1, 11, 2, 4, 3]
test_resultados = [28, 29, 31, 30, 29, 30, None]

for i in range(len(test_anios)):
    an = test_anios[i]
    me = test_meses[i]

    print(an, me, "->", end=" ")
    resultado = dias_en_mes(an, me)
    if resultado == test_resultados[i]:
        print("OK")
    else:
        print("Fallido")

def dias_anio(anio, mes, dia):
    if anio < 1 or mes < 1 or mes > 12:
        return None

    dim = dias_en_mes(anio, mes)

    if dia < 1 or dia > dim:
        return None
    total_dias = dia
    for m in range(1, mes):
        total_dias += dias_en_mes(anio, m)
    return total_dias

print(dias_anio(2000, 12, 31))
    