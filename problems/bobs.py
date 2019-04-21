# Showing the number of bobs in a word
word = input('Enter a word: ')
bobs_count = 0

for i in range(len(word)):
    if word[i] == 'b' and i < len(word) - 2:
        if word[i+1] == 'o' and word[i+2] == 'b':
            bobs_count += 1

print('The number of bobs in this word is:', bobs_count)
    

