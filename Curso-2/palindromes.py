#LAB Modulo 2- Sección 5
#Improving the Caesar cipher
# Python essentials 2


text = input("Enter text: ")

text = text.replace(' ','')

if len(text) > 1 and text.upper() == text[::-1].upper():
	print("It's a palindrome")
else:
	print("It's not a palindrome")