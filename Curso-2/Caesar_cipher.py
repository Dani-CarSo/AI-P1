#LAB Modulo 2- Sección 5
#Improving the Caesar cipher
# Python essentials 2

text = input("Enter message: ")

while True:
    try:
        shift = int(input("Enter the cipher shift value (1..25): "))
        if shift in range(1, 26):
            break
        print("Incorrect shift value!")
    except ValueError:
        print("Incorrect shift value!")

cipher = ''

for char in text:
    if char.isalpha():
        code = ord(char) + shift
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
    
        code -= first
        code %= 26
        cipher += chr(first + code)
    else:
        cipher += char

print(cipher)