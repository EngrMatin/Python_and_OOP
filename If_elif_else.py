marks = int(input("Enter total marks: "))

if marks >= 600 and marks <=1000:
    print("First Division")
elif marks >= 450 and marks < 600:
    print("Second Division")
elif marks >= 333 and marks < 450:
    print("Third Division")
elif marks >= 0 and marks < 333:
    print("Failed!")
else:
    print("Invalid marks!")

