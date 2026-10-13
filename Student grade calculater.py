print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")
subjects = ["Python", "Mathematics", "Physics", "Chemistry", "English"]

marks = []
total = 0

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks in {subject} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                total += mark
                break
            else:
                print("Invalid marks! Enter between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

percentage = total / len(subjects)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 35:
    grade = "E"
else:
    grade = "F"

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/", len(subjects) * 100)
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)

if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
