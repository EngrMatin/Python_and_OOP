file = open('words.dat', 'w') 
word = '' 

while True: 
    word = input('Enter a word (press ENTER or SPACE bar to quit): ') 
    
    file.write(word + '\n')
    if word == '' or word == ' ':
        break
     
file.close()