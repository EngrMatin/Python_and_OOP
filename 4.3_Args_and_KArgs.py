def add(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

result = add(1,2,3,4,5)
print(result)

def all_types(first, *args, **kargs):
    print(first)

    print(args)
    for i in args:
        print(i)
        
    print(kargs)
    for key, value in kargs.items():
        print(key, value)

all_types('aaa', 'bbb', 'ccc', 'ddd', name='sakib', father='rakib')