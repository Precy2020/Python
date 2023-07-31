def students(male_or_female):
    female = 0
    male = 0
    change = []
    for index in male_or_female:
        if index == 'male'.casefold():
            male = 1
            change = male
        elif index == 'female'.casefold():
            female = 1
            change = female
    return change


student = ('Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male',
           'female')
print(students(student))

