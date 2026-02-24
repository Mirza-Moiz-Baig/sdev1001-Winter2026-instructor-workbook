word = input("Enter a word for us to count vowels: ")
vowels = 'aeiou'
total = 0
for each_character in word:
    print(each_character)
    if each_character.lower() in vowels:
        total += 1
print(f"There are {total} vowels in {word}")
