file = open('words.dat', 'w') 
word = '' 

while word != 'END': 
    word = input('Enter a word (enter END to quit): ') 
    file.write(word + '\n')

file.close()

words = open('words.dat', 'r').readlines()
for i in range(len(words)):
    print(f'{i+1}: {words[i]}')

file.close()