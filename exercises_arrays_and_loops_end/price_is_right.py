import random
Randoms_Prices = [
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10)
]
breakpoint()
print('"Welcome to the Price is Right! Guess the price of this coffee"')
User_guess = int(input('Guess the price of the item:'))

if  User_guess in Randoms_Prices:
    print("You win!")
else:
    print("You loose!")
print('The price were:')
print(Randoms_Prices)