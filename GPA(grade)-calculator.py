# Define letter grades and corresponding grade points
letter_grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D','F']
grade_points = [4.0, 4.0, 3.75, 3.5,3.0,2.75,2.5,2.0,1.75,1.0, 0]

# Print letter grades with corresponding grade points
print("Letter Grades and Corresponding Grade Points:")
for letter, point in zip(letter_grades, grade_points):
    print(f"{letter}: {point}")
print("\n")

# Input: Number of courses
number_of_courses = int(input("Enter the number of courses: "))

# Initialize lists to store marks and credit hours
marks = []
credit_hours = []
print("\n")

# Accept marks for each course
for i in range(number_of_courses):
    mark = float(input(f"Enter mark for course {i + 1}: "))
    marks.append(mark)

# Print marks
print("Marks:", marks)
print("\n")

# Accept credit hours for each course
for i in range(number_of_courses):
    credit_hour=float(input(f"Enter credit hour for course {i + 1}: "))
    credit_hours.append(credit_hour)

print("\n")

# Initialize total grade points and total credit hours
total_grade_points = 0
total_credit_hours = sum(credit_hours)

# Loop through each course to calculate GPA and print details
for i in range(len(marks)):
    if 90 <= marks[i] <= 100:
        grade = letter_grades[0]
    elif 85 <= marks[i] <= 89:
        grade = letter_grades[1]
    elif 80 <= marks[i] <= 84:
        grade = letter_grades[2]
    elif 75 <= marks[i] <= 79:
        grade = letter_grades[3]
    elif 70 <= marks[i] <= 74:
        grade = letter_grades[4]
    elif 65 <= marks[i] <= 69:
        grade = letter_grades[5]
    elif 60 <= marks[i] <= 64:
        grade = letter_grades[6]
    elif 50 <= marks[i] <= 59:
        grade = letter_grades[7]
    elif 45 <= marks[i] <= 49:
        grade = letter_grades[8]
    elif 40 <= marks[i] <= 44:
        grade = letter_grades[9]
    elif 0 <= marks[i] <= 39:
        grade = letter_grades[10]
    else:
        grade = "Invalid mark"

    # Print course details
    print(f"Course {i + 1}, Mark: {marks[i]}, Grade: {grade}, Credit Hour: {credit_hours[i]}")

    # Calculate total grade points
    if grade != "Invalid mark":
        total_grade_points += grade_points[letter_grades.index(grade)] * credit_hours[i]

# Calculate and print GPA
gpa = total_grade_points / total_credit_hours
print(f"\nGPA: {gpa:.2f}")