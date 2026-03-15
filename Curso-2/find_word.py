#LAB Modulo 2- Sección 5
#Find the Word  
# Python essentials 2

word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()
found = True
start = 0

for letter in word:
    pos = strn.find(letter, start)  
    if pos == -1:
        found = False   
        break
    start = pos + 1     

if found:
    print("Yes")
else:
    print("No")