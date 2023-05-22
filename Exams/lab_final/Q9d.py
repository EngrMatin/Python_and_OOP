file = open('words.dat', 'w') 
word = '' 

while True: 
    word = input('Enter a word (enter END to quit): ') 
    if word == 'END':
        break
    file.write(word + '\n')
     
file.close()