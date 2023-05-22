student_name = input("Enter student's name: ")
marks = float(input("Enter the marks: "))
student_id = input("Enter student's ID: ")

filepath = 'E:\Phitron\Python\\' + student_id + '.txt'

with open(filepath, 'w') as fp:
    fp.write(f'Name: {student_name} ')
    fp.write(f' Marks: {marks}')
    fp.close()
