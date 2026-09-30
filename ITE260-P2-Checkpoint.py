def average(student1, student2, student3):
    return(student1 + student2 + student3)/3

student = int(input("How many students will be processed? "))

if student <3:
    student = 3

for i in range(student):
    print()
    print("Student", i + 1)

    name = input("Enter your Name: ")
    student1 = float(input("Activity 1: "))
    student2 = float(input("Activity 2: "))
    student3 = float(input("Activity 3: "))

    result = average(student1, student2, student3)

    if result >= 90:
        status = "Excellent"
    elif result >= 80:
        status = "Very Good"
    elif result >= 75:
        status = "Passed"
    else:
        status = "Failed"

    print()
    print("NAME:", name)
    print("Activity1:", student1)
    print("Activity2:", student2)
    print("Activity3:", student3)
    print("Average:", round(result, 2))
    print("Status:", status)