#LAB Modulo 2- Sección 5
#The Digit Life
# Python essentials 2

date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")


if len(date) == 8 and date.isdigit():
    while len(date) > 1:
        total = sum(int(d) for d in date)
        date = str(total)
    
    print("Your Digit of Life is: " + date)

else:
    print("Invalid date format. Please enter exactly 8 digits.")