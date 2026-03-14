#LAB Modulo 3- Sección 8
# Proyecto de módulo 3
# Python essentials 1

print("Tic Tac Toe")
from pickle import TRUE
from random import randrange

tablero = [[1,2,3],
          [4,'X',6],
          [7,8,9]]

def display_tablero(tablero):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(tablero[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")
  
def avance(tablero):
    ok = False
    while not ok:
        move = int(input("Ingresa tu movimiento: "))
        if move >= 1 and move <= 9:
            row = (move-1)//3
            col = (move-1)%3
            if board[row][col] not in ['O','X']:
                board[row][col] = 'O'
                ok = True
            else:
                print("Cuadro ocupado, intenta de nuevo")
        else:
            print("Movimiento inválido, intenta de nuevo")

def computadora(tablero):
    free = []
    for row in range(3):
        for col in range(3):
            if tablero[row][col] not in ['O','X']:
                free.append((row,col))
                return free
        
def ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2]:
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i]:
            return tablero[0][i]
    if tablero[0][0] == tablero[1][1] == tablero[2][2]:
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return tablero[0][2]
    return False

def movimiento_computadora(tablero):
    free = computadora(tablero)
    if len(free) > 0:
        move = randrange(len(free))
        row, col = free[move]
        tablero[row][col] = 'X'
        while TRUE:
            if ganador(tablero) == 'X':
                print("¡Nimodo, te humillaron, gano la maquina!")
                break
            elif ganador(tablero) == 'O':
                print("¡Felicidades, ganaste!")
                break
            elif len(computadora(tablero)) == 0:
                print("¡Empate!")
                break
            else:
                avance(tablero)
                display_tablero(tablero)