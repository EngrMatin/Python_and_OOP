import pyjokes
def tell_some_jokes():

    My_joke = pyjokes.get_joke(language="en", category="all")
    print(My_joke)

greet_words = ['hi', 'hi!' 'hello', 'yo', 'yeh' ]
bye_words = ['bye', 'bye-bye', 'ta-ta']
bad_words = ['bad', 'notty', 'bustard', 'bitch']
entertainment = ['joke', 'jokes']

def listen():
    return input("Say something: ")

def decide(command):
    command = command.lower()
    words = command.split()

    for word in words:
        if word in greet_words:
            print("Hi man")
            break

        elif word in bye_words:
            print("Take care! bye!")
            exit()

        elif word in bad_words:
            print("You are a bad guy. Behave yourself")
            break

        elif word in entertainment:
            #tell_some_jokes()
            talkback(word)
            break 
    

def talkback(response):
    tell_some_jokes()
    #print(response)

while True:
    command = listen()
    decide(command)