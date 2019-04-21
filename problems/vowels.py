# Showing the number of vowels in a word
word = input('Enter a word: ')
vowels = ['a','e','i','o','u']
vowels_count = 0

for i in range(len(word)):
    for j in range(len(vowels)):
        if (vowels[j] == word[i]):
            vowels_count += 1

print('The number of vowels in this word is:', vowels_count)

