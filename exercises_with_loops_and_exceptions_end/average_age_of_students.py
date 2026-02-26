print("Average age of students calculator")
age_count=0
student_count=0
while True:
    age = input("Enter the age of a student or 'stop' to finish:")
    if age == "stop":
        break
    else: 
        try:
            age_count += int(age)
            student_count += 1
        except ValueError:
            print("Please enter a number or 'stop' to finish")
try:
    print(f"The average age of the students is  {age_count/student_count}")
except ZeroDivisionError:
    print("You didn't enter any ages")

