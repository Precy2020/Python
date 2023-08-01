def students(gender):

    change = {'male': 0, 'female': 0}
    for index in gender:
        if index.casefold() == 'male':
            change['male'] += 1

        elif index.casefold() == 'female':
            change['female'] += 1

    return list(change.items())


student = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male',
           'female']
print(students(student))

