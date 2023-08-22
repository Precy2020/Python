students = 0
subjects = 0
score = []
total = []
average = []
position = []


def collect_user_input():
    global students
    global subjects
    global score

    students = (int(input('How many students do you have? ')))
    subjects = (int(input('How many subject do they offer? ')))
    for number in range(students):
        score.append([])
        for numbers in range(subjects):
            print("Entering score for ", number + 1, '\n' "Enter score for subject ", numbers + 1)
            scores = input("Score: ")

            score[number].append(scores)


collect_user_input()


def summary():
    global score
    global students
    global subjects
    global total

    print("STUDENT    ", end="")
    for i in range(subjects):
        print("SUB", i + 1, "  ", end="")
    print("TOT", "   ", "AVE", "   ", "POS")
    for i in range(students):
        print("Student", i + 1, end="   ")
        for j in range(subjects):
            print(score[i][j], end="    ")
            print()
            print(sum(score))


summary()
