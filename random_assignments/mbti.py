name = input('Enter name > ')
count_Ei_A = 0
count_Ei_B = 0
count_SN_A = 0
count_SN_B = 0
count_TF_A = 0
count_TF_B = 0
count_JP_A = 0
count_JP_B = 0

selection = [
    ["A. Expend energy, enjoy groups ", "B. Conserve energy, one-on-one" + '\n'],
    ["A. Interpret literally ", "B. Look for meaning and possibilities" + '\n'],
    ["A. Logical, thinking, questioning ", "B. Empathetic, feeling, accommodating" + '\n'],
    ["A. Organized, orderly ", "B. Flexible, adaptable" + '\n'],
    ["A. More outgoing, think out loud ", "B. More reserved, think to yourself" + '\n'],
    ["A. Practical, realistic, experiential ", "B. Imagination, innovative, theoretical" + '\n'],
    ["A. Candid, straight forward, frank ", "B. Tactful, kind, encouraging" + '\n'],
    ["A. Plan, schedule ", "B. Unplanned, spontaneous" + '\n'],
    ["A. seek many tasks, public activities, interaction with others ",
     "B. seek private, solitary activities with quiet to concentrate" + '\n'],
    ["A. standard, usual, conventional ", "B. different, novel, unique" + '\n'],
    ["A. firm, tend to criticize, hold the line ", "B. gentle, tend to appreciate, conciliate" + '\n'],
    ["A.regulated, structured ", "B. easygoing, live  and let live" + '\n'],
    ["A. external, communicative, express yourself ", "B. internal, reticent, keep to yourself" + '\n'],
    ["A. focus on here-and-now ", "B. look to the future, global perspective, \"big picture\"" + '\n'],
    ["A. tough minded, just ", "B. tender-hearted, merciful" + '\n'],
    ["A. preparation, plan ahead ", "B. go with the flow, adapt as you go" + '\n'],
    ["A. active, initiate ", "B. reflective, deliberate" + '\n'],
    ["A. facts, things, \"what is\" ", "B. ideas, dreams, 'what could be', philosophical" + '\n'],
    ["A. matter of fact, issue oriented ", "B. sensitive, people-oriented, compassionate" + '\n'],
    ["A. control, govern ", "B. latitude, freedom" + '\n']]


def first():
    query1 = input(selection[0][0] + ' \t' + selection[0][1])
    if query1.casefold() == 'a':
        second()
    elif query1.casefold() == 'b':
        second()
    else:
        print('Not valid dear :)! try again')
        first()


def second():
    query2 = input(selection[1][0] + ' \t' + selection[1][1])
    if query2.casefold() == 'a':
        third()
    elif query2.casefold() == 'b':
        third()
    else:
        print('Not valid dear :)! try again')
        second()


def third():
    query3 = input(selection[2][0] + ' \t' + selection[2][1])
    if query3.casefold() == 'a' or query3.casefold() == 'b':
        forth()
    else:
        print('Not valid dear :)! try again')
        third()


def forth():
    query4 = input(selection[3][0] + ' \t' + selection[3][1])
    if query4.casefold() == 'a' or query4.casefold() == 'b':
        fifth()
    else:
        print('Not valid dear :)! try again')
        forth()


def fifth():
    query5 = input(selection[4][0] + ' \t' + selection[4][1])
    if query5.casefold() == 'a' or query5.casefold() == 'b':
        sixth()
    else:
        print('Not valid dear :)! try again')
        fifth()


def sixth():
    query6 = input(selection[5][0] + ' \t' + selection[5][1])
    if query6.casefold() == 'a' or query6.casefold() == 'b':
        seventh()
    else:
        print('Not valid dear :)! try again')
        sixth()


def seventh():
    query7 = input(selection[6][0] + ' \t' + selection[6][1])
    if query7.casefold() == 'a' or query7.casefold() == 'b':
        eighth()
    else:
        print('Not valid dear :)! try again')
        seventh()


def eighth():
    query8 = input(selection[7][0] + ' \t' + selection[7][1])
    if query8.casefold() == 'a' or query8.casefold() == 'b':
        ninth()
    else:
        print('Not valid dear :)! try again')
        eighth()


def ninth():
    query9 = input(selection[8][0] + ' \t' + selection[8][1])
    if query9.casefold() == 'a' or query9.casefold() == 'b':
        tenth()
    else:
        print('Not valid dear :)! try again')
        ninth()


def tenth():
    query10 = input(selection[9][0] + ' \t' + selection[9][1])
    if query10.casefold() == 'a' or query10.casefold() == 'b':
        eleventh()
    else:
        print('Not valid dear :)! try again')
        tenth()


def eleventh():
    query11 = input(selection[10][0] + ' \t' + selection[10][1])
    if query11.casefold() == 'a' or query11.casefold() == 'b':
        twelfth()
    else:
        print('Not valid dear :)! try again')
        eleventh()


def twelfth():
    query12 = input(selection[11][0] + ' \t' + selection[11][1])
    if query12.casefold() == 'a' or query12.casefold() == 'b':
        thirteenth()
    else:
        print('Not valid dear :)! try again')
        twelfth()


def thirteenth():
    query13 = input(selection[12][0] + ' \t' + selection[12][1])
    if query13.casefold() == 'a' or query13.casefold() == 'b':
        fourteenth()
    else:
        print('Not valid dear :)! try again')
        thirteenth()


def fourteenth():
    query14 = input(selection[13][0] + ' \t' + selection[13][1])
    if query14.casefold() == 'a' or query14.casefold() == 'b':
        fifteenth()
    else:
        print('Not valid dear :)! try again')
        fourteenth()


def fifteenth():
    query15 = input(selection[14][0] + ' \t' + selection[14][1])
    if query15.casefold() == 'a' or query15.casefold() == 'b':
        sixteenth()
    else:
        print('Not valid dear :)! try again')
        fifteenth()


def sixteenth():
    query16 = input(selection[15][0] + ' \t' + selection[15][1])
    if query16.casefold() == 'a' or query16.casefold() == 'b':
        seventeenth()
    else:
        print('Not valid dear :)! try again')
        sixteenth()


def seventeenth():
    query17 = input(selection[16][0] + ' \t' + selection[16][1])
    if query17.casefold() == 'a' or query17.casefold() == 'b':
        eighteenth()
    else:
        print('Not valid dear :)! try again')
        seventeenth()


def eighteenth():
    query18 = input(selection[17][0] + ' \t' + selection[17][1])
    if query18.casefold() == 'a' or query18.casefold() == 'b':
        nineteenth()
    else:
        print('Not valid dear :)! try again')
        eighteenth()


def nineteenth():
    query19 = input(selection[18][0] + ' \t' + selection[18][1])
    if query19.casefold() == 'a' or query19.casefold() == 'b':
        twentieth()
    else:
        print('Not valid dear :)! try again')
        nineteenth()


def twentieth():
    query20 = input(selection[19][0] + ' \t' + selection[19][1])
    if query20.casefold() == 'a' or query20.casefold() == 'b':
        print('Thanks!!')
    else:
        print('Not valid dear :)! try again')
        twentieth()


def main():
    first()


main()



