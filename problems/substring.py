# Showing the biggest substring in alphabetical order
word = input('Enter a word: ')
new_word = ''
words = []
temp = ''

for i in word:
    if i >= temp:
        temp = i
        new_word += i
    else:
        words.append(new_word)
        new_word = i
        temp = i
        
words.append(new_word)
        
print(max(words, key=len))
