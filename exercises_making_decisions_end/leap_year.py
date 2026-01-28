user_input = input("Enter a year:")
year_guess =int(user_input)
if ((year_guess % 4) == 0) and ((year_guess % 100) != 0) or ((year_guess%400)== 0):
    print(F"{year_guess} is a leap year? True")
else:
    print(F"{year_guess} is a leap year? False")