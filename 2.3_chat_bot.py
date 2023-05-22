greet_words = ['hi', 'hello', 'yo', 'yeh' ]
bye_words = ['bye', 'bye-bye', 'ta-ta']
bad_words = ['bad', 'notty', 'bustard', 'bitch']

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
            print("Ta-ta bye-bye")
            break

        elif word in bad_words:
            print("You are a bad guy. Behave yourself")
            break
    

def talkback(response):
    print(response)

while True:
    command = listen()
    decide(command)
