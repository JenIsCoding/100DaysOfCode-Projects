# Determine the High Score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest = 0
for n in range(0, len(student_scores)):
    if student_scores[n] >= highest:
        highest = student_scores[n]
    else:
      highest = highest

print(f"The highest score in the class is: {highest}")