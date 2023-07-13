
total = 0
counter = 0
number_of_student = 0

while counter < 20:
    grade = int(input('Enter grade, 1 to 20: '))
    if grade < 0:
        print("This is an invalid value")

    total = total + grade
    counter = counter + 1

average = total / counter
print("********************************************************************")
print('\t''\t''\t'"Aso Rock Secondary School, Abuja Nigeria")
print("********************************************************************")
print('Class: SSS 3')
print("Number of Student in class: ", counter)
print('Total Score', total)
print('Average', average)
