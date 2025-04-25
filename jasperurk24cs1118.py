student1 = {
    "name": "John",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0, 87.0]
}

student2 = {
    "name": "Vicky",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0, 75.0]
}

student3 = {
    "name": "Joel",
    "homework": [20.0, 87.0, 75.0, 22.0],
    "quizzes": [35.0, 75.0, 78.0],
    "tests": [100.0, 98.0, 78.0]
}

batch = [student1, student2, student3]

# Loop through each student and compute their grades
for student in batch:
    print("Name:", student['name'])
    print("Homework:", student['homework'])
    print("Quizzes:", student['quizzes'])
    print("Tests:", student['tests'])

    avg_homework = sum(student["homework"]) / len(student["homework"])
    avg_quizzes = sum(student["quizzes"]) / len(student["quizzes"])
    avg_tests = sum(student["tests"]) / len(student["tests"])

    total_avg = (avg_homework + avg_quizzes + avg_tests) / 3
    print("Total Average:", round(total_avg, 2))

    # Assign grade
    if total_avg >= 90:
        grade = "A"
    elif total_avg >= 80:
        grade = "B"
    elif total_avg >= 70:
        grade = "C"
    elif total_avg >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)
    print("-" * 40)



