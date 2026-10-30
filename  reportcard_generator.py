print("=" * 40) # result info
print("First Year's Results")
print("=" * 40)

def score_to_grade(score):# converting score to grade
    if 70 <= score <= 100:
        grade = "A"
    elif 60 <= score <= 69:
        grade = " B"
    elif 50 <= score <= 59:
        grade = "C"
    elif 40 <= score <= 49:
        grade = "D"
    elif 0 <= score <= 39:
        grade = "E"
    return grade
names = []
grades = []
sum_score = 0
num_students = int(input("Enter entire class population:")) #class population 
teacher_remarks= str(input("Enters a short report:"))

for student in range(num_students):# recording students names and their respective score
    student = str(input("enter student's name:"))
    score = int(input("enter student's score:"))
    sum_score += score
    letter_grade = score_to_grade(score)
    names.append(student)
    grades.append(letter_grade)
for i in range(len(names)):
    print(f"{names[i]}: {grades[i]}")

average = sum_score/num_students # finding average score of the class 

print(f"Class average score:{average:.2f}")
        
        
