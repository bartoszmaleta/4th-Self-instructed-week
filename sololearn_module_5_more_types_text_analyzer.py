filename = input("Enter a filename: ")


with open(filename) as f:
    text = f.read()

print(text)


def count_char(text, char):
    count = 0
    
    for letter in text:
        if letter == char:
            count += 1
    
    return count


print('------------------------------------------------ \nCounts how many times a character occurs in a string:')
occured_character = 'r'
print('The letter is {}'.format(occured_character))

print(count_char(text, occured_character))


print('------------------------------------------------ \nCounts What percentage of the text each character of the alphabet occupies:')
alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
    percentage_of_character_appearence = 100 * count_char(text, char) / len(text)
    print('{} - {}\n'.format(char, round(percentage_of_character_appearence, 2)))

