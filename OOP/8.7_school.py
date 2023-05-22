class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class School:
    def __init__(self, name, teachers, courses, students):
        self.name = name
        self.teachers = teachers
        self.courses = courses
        self.students = students

    def get_students(self):
        for student in self.students:
            print(student.name)    

school_name = 'Phitron'
ds_course = Course('Data Structure', 'Einstein')
teacher1 = Teacher('Einstein', ds_course)
algo_course = Course('Algorithm', 'Edison')
teacher2 = Teacher('Edison', algo_course)

student1 = Student('Rohmot', 19, 45)
student2 = Student('Kudrot', 17, 33)
student3 = Student('Torikot', 23, 72)

teachers = [teacher1, teacher2]
courses = [ds_course, algo_course]
students = [student1, student2, student3]

my_school = School(school_name, teachers, courses, students)

my_school.get_students()

        
