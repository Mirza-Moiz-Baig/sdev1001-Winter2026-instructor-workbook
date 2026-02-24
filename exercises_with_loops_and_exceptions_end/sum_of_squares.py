my_square = int(input("Enter a number to sum the squares:"))
total = 0
for number in range(my_square):
    total += (number+1)**2
print(f'The sum of squares is: {total}')