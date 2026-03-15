#LAB Modulo 2- Sección 3
# Seven-segment display
# Python essentials 2

Digits= [
    ["###","# #","# #","# #","###"], #0
    ["  #","  #","  #","  #","  #"], #1     
    ["###","  #","###","#  ","###"], #2
    ["###","  #","###","  #","###"], #3
    ["# #","# #","###","  #","  #"], #4
    ["###","#  ","###","  #","###"], #5
    ["###","#  ","###","# #","###"], #6
    ["###","  #","  #","  #","  #"], #7
    ["###","# #","###","# #","###"], #8
    ["###","# #","###","  #","###"]  #9
]

def display_number(number):
    digits= [Digits[int(digit)] for digit in str(number)]
    for row in range(5):
         print(" ".join(digit[row] for digit in digits))
number = input("Enter a non-negative integer: ")
display_number(number)
