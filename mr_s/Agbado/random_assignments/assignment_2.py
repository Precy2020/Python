# sentinel

total = 1
grade = 1
number_of_student = 1

while grade != -1:
    grade = int(input('Enter grade: '))
    total = total + grade
    grade = grade + 1

    if grade == " ":
        print('No input found!')

average = total / grade
print("********************************************************************")
print('\t''\t''\t'"Aso Rock Secondary School, Abuja Nigeria")
print("********************************************************************")
print('Class: SSS 3')
print("Number of Student in class: ", grade)
print('Total Score', total)
print('Average', average)
