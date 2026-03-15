#LAB Modulo 2- Sección 5
#Anagrams
# Python essentials 2

str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

if str_1.strip() == '' and str_2.strip() == '':
    print("Not anagrams")
else:
    processed_1 = ''.join(sorted(str_1.replace(' ', '').upper()))
    processed_2 = ''.join(sorted(str_2.replace(' ', '').upper()))

    if processed_1 == processed_2:
        print("Anagrams")
    else:
        print("Not anagrams")