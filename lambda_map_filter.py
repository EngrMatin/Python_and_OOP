def square(x):
    return x*x

result = square(6)
print(result)

# equivalent function with Lambda
square2 = lambda x: x*x

result2 = square2(8)
print(result2)


list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def double_it(x):
    return x*2

# equivalent function with Lambda
double_it = lambda x: x*2

map2 = map(double_it, list1)
list2 = list(map2)
print(list2)


map3 = map(lambda x: x*x, list1)
print(list(map3))


map4 = filter(lambda x: x>50, list1)
print(list(map4))


actors= [{'name': 'sakib', 'age': 34}, 
         {'name': 'manna', 'age': 51},
         {'name': 'sabana', 'age': 65},
         {'name': 'bubli', 'age': 30},]

senior_actors = filter(lambda actor: actor['age']>35, actors)
print(list(senior_actors))

junior_actors = filter(lambda actor: actor['age']<35, actors)
print(list(junior_actors))