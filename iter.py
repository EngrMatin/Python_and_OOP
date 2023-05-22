numbers = [12, 45, 23, 65, 89, 78, 11, 82]
num_iter = iter(numbers)
try:
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
except StopIteration:
    print("Iteration is stopped")