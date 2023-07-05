total = 0
grade = int(input('Enter grade: '))
for grade in range(21):
    grade = int(input('Enter grade: '))
    if grade < 0:
        print("This is an invalid value")

    total = total + grade
average = total / grade
print(f'''********************************************************************
                   Aso Rock Secondary School, Abuja Nigeria
          ********************************************************************
                         Class: SSS 3
                 Number of Student in class:  {grade}
                 Total Score:                 {total}
                 Average:                     {average}
       **1**************************************************************
''')