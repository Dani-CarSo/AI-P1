#LAB Modulo 2- Sección 5
#Sudoku
# Python essentials 2

def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]

rows = []
for r in range(9):
    row = input()
    if len(row) != 9 or not all(c in '123456789' for c in row):
        print("Invalid input")
        exit()
    rows.append(row)

ok = True

for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

if ok:
    for c in range(9):
        if not checkset(rows[r][c] for r in range(9)):
            ok = False
            break

if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square = [rows[r + dr][c + dc] for dr in range(3) for dc in range(3)]
            if not checkset(square):
                ok = False
                break

if ok:
    print("Yes")
else:
    print("No")