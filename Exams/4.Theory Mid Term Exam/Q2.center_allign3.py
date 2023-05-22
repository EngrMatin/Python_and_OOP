def center_align(filename, width):
    lines = open(filename, 'r').readlines()

    for line in lines:
        print(line.center(width))

filename = input("Enter the file name: ")
width = int(input("Enter the width of the file: "))

center_align(filename, width)