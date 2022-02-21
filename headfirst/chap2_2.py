vowels = ['a','e','i','o','u']

word = input('Provive a word to sarrch for vowels:')

found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

print(found)


# vowels = ['a','e','i','o','u']

# word = 'Milliways'

# found = []

# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print(vowel)

