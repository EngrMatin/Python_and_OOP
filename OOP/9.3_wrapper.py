def do_something(work):
    print('Starting the work')
    work()
    print('Done successfully')

def practice_coding():
    print('I am practicing Python')

def learn_surfing():
    print('I am learning surfing')

do_something(practice_coding)
do_something(learn_surfing)
print('\n')

def outer_function():
    print('inside the outer function')
    def inner_function():
        print('inside the inner function')
    inner_function()

outer_function()
print('\n')

def first_function():
    print('inside the first function')
    def second_function():
        print('inside the second function')
    return second_function

check = first_function()
print('\n')

check()
print('\n')

first_function()()