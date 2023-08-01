name = input('Enter name > ')
name_responses = []
count_Ei_A = 0
count_Ei_B = 0
count_SN_A = 0
count_SN_B = 0
count_TF_A = 0
count_TF_B = 0
count_JP_A = 0
count_JP_B = 0

ei_responses = []
sn_responses = []
tf_responses = []
jp_responses = []

personality_type = []
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
    global ei_responses
    global count_Ei_A
    global count_Ei_B
    query1 = input(selection[0][0] + ' \t' + selection[0][1])
    if query1.casefold() == 'a':
        count_Ei_A += 1
        ei_responses.append(selection[0][0])

        second()
    elif query1.casefold() == 'b':
        count_Ei_B += 1
        ei_responses.append(selection[0][1])
        second()
    else:
        print('Not valid dear :)! try again')
        first()


def second():
    global sn_responses
    global count_SN_A
    global count_SN_B
    query2 = input(selection[1][0] + ' \t' + selection[1][1])
    if query2.casefold() == 'a':
        count_SN_A += 1
        sn_responses.append(selection[1][0])
        third()
    elif query2.casefold() == 'b':
        count_SN_B += 1
        sn_responses.append(selection[1][1])
        third()
    else:
        print('Not valid dear :)! try again')
        second()


def third():
    global tf_responses
    global count_TF_A
    global count_TF_B
    query3 = input(selection[2][0] + ' \t' + selection[2][1])
    if query3.casefold() == 'a':
        count_TF_A += 1
        tf_responses.append(selection[2][0])
        forth()
    elif query3.casefold() == 'b':
        count_TF_B += 1
        tf_responses.append(selection[2][1])
        forth()
    else:
        print('Not valid dear :)! try again')
        third()


def forth():
    global jp_responses
    global count_JP_A
    global count_JP_B
    query4 = input(selection[3][0] + ' \t' + selection[3][1])
    if query4.casefold() == 'a':
        count_JP_A += 1
        jp_responses.append(selection[3][0])
        fifth()
    elif query4.casefold() == 'b':
        count_JP_B += 1
        jp_responses.append(selection[3][1])
        fifth()
    else:
        print('Not valid dear :)! try again')
        forth()


def fifth():
    global ei_responses
    global count_Ei_A
    global count_Ei_B
    query5 = input(selection[4][0] + ' \t' + selection[4][1])
    if query5.casefold() == 'a':
        count_Ei_A += 1
        ei_responses.append(selection[4][0])
        sixth()
    elif query5.casefold() == 'b':
        count_Ei_B += 1
        ei_responses.append(selection[4][1])
        sixth()
    else:
        print('Not valid dear :)! try again')
        fifth()


def sixth():
    global sn_responses
    global count_SN_A
    global count_SN_B
    query6 = input(selection[5][0] + ' \t' + selection[5][1])
    if query6.casefold() == 'a':
        count_SN_A += 1
        sn_responses.append(selection[5][0])
        seventh()
    elif query6.casefold() == 'b':
        count_SN_B += 1
        sn_responses.append(selection[5][1])
        seventh()
    else:
        print('Not valid dear :)! try again')
        sixth()


def seventh():
    global tf_responses
    global count_TF_A
    global count_TF_B
    query7 = input(selection[6][0] + ' \t' + selection[6][1])
    if query7.casefold() == 'a':
        count_TF_A += 1
        tf_responses.append(selection[6][0])
        eighth()
    elif query7.casefold() == 'b':
        count_TF_B += 1
        tf_responses.append(selection[6][1])
        eighth()
    else:
        print('Not valid dear :)! try again')
        seventh()


def eighth():
    global jp_responses
    global count_JP_A
    global count_JP_B
    query8 = input(selection[7][0] + ' \t' + selection[7][1])
    if query8.casefold() == 'a':
        count_JP_A += 1
        jp_responses.append(selection[7][0])
        ninth()
    elif query8.casefold() == 'b':
        count_JP_B += 1
        jp_responses.append(selection[7][1])
        ninth()
    else:
        print('Not valid dear :)! try again')
        eighth()


def ninth():
    global ei_responses
    global count_Ei_A
    global count_Ei_B
    query9 = input(selection[8][0] + ' \t' + selection[8][1])
    if query9.casefold() == 'a':
        count_Ei_A += 1
        ei_responses.append(selection[8][0])
        tenth()
    elif query9.casefold() == 'b':
        count_Ei_B += 1
        ei_responses.append(selection[8][1])
        tenth()
    else:
        print('Not valid dear :)! try again')
        ninth()


def tenth():
    global sn_responses
    global count_SN_A
    global count_SN_B
    query10 = input(selection[9][0] + ' \t' + selection[9][1])
    if query10.casefold() == 'a':
        count_SN_A += 1
        sn_responses.append(selection[9][0])
        eleventh()
    elif query10.casefold() == 'b':
        count_SN_B += 1
        sn_responses.append(selection[9][1])
        eleventh()
    else:
        print('Not valid dear :)! try again')
        tenth()


def eleventh():
    global tf_responses
    global count_TF_A
    global count_TF_B
    query11 = input(selection[10][0] + ' \t' + selection[10][1])
    if query11.casefold() == 'a':
        count_TF_A += 1
        tf_responses.append(selection[10][0])
        twelfth()
    elif query11.casefold() == 'b':
        count_TF_B += 1
        tf_responses.append(selection[10][1])
        twelfth()
    else:
        print('Not valid dear :)! try again')
        eleventh()


def twelfth():
    global jp_responses
    global count_JP_A
    global count_JP_B
    query12 = input(selection[11][0] + ' \t' + selection[11][1])
    if query12.casefold() == 'a':
        count_JP_A += 1
        jp_responses.append(selection[11][0])
        thirteenth()
    elif query12.casefold() == 'b':
        count_JP_B += 1
        jp_responses.append(selection[11][1])
        thirteenth()
    else:
        print('Not valid dear :)! try again')
        twelfth()


def thirteenth():
    global ei_responses
    global count_Ei_A
    global count_Ei_B
    query13 = input(selection[12][0] + ' \t' + selection[12][1])
    if query13.casefold() == 'a':
        count_Ei_A += 1
        ei_responses.append(selection[12][0])
        fourteenth()
    elif query13.casefold() == 'b':
        count_Ei_B += 1
        ei_responses.append(selection[12][1])
        fourteenth()
    else:
        print('Not valid dear :)! try again')
        thirteenth()


def fourteenth():
    global sn_responses
    global count_SN_A
    global count_SN_B
    query14 = input(selection[13][0] + ' \t' + selection[13][1])
    if query14.casefold() == 'a':
        count_SN_A += 1
        sn_responses.append(selection[13][0])
        fifteenth()
    elif query14.casefold() == 'b':
        count_SN_B += 1
        sn_responses.append(selection[13][1])
        fifteenth()
    else:
        print('Not valid dear :)! try again')
        fourteenth()


def fifteenth():
    global tf_responses
    global count_TF_A
    global count_TF_B
    query15 = input(selection[14][0] + ' \t' + selection[14][1])
    if query15.casefold() == 'a':
        count_TF_A += 1
        tf_responses.append(selection[14][0])
        sixteenth()
    elif query15.casefold() == 'b':
        count_TF_B += 1
        tf_responses.append(selection[14][1])
        sixteenth()
    else:
        print('Not valid dear :)! try again')
        fifteenth()


def sixteenth():
    global jp_responses
    global count_JP_A
    global count_JP_B
    query16 = input(selection[15][0] + ' \t' + selection[15][1])
    if query16.casefold() == 'a':
        count_JP_A += 1
        jp_responses.append(selection[15][0])
        seventeenth()
    elif query16.casefold() == 'b':
        count_JP_B += 1
        jp_responses.append(selection[15][1])
        seventeenth()
    else:
        print('Not valid dear :)! try again')
        sixteenth()


def seventeenth():
    global ei_responses
    global count_Ei_A
    global count_Ei_B
    query17 = input(selection[16][0] + ' \t' + selection[16][1])
    if query17.casefold() == 'a':
        count_Ei_A += 1
        ei_responses.append(selection[16][0])
        eighteenth()
    elif query17.casefold() == 'b':
        count_Ei_B += 1
        ei_responses.append(selection[16][1])
        eighteenth()
    else:
        print('Not valid dear :)! try again')
        seventeenth()


def eighteenth():
    global sn_responses
    global count_SN_A
    global count_SN_B
    query18 = input(selection[17][0] + ' \t' + selection[17][1])
    if query18.casefold() == 'a':
        count_SN_A += 1
        sn_responses.append(selection[17][0])
        nineteenth()
    elif query18.casefold() == 'b':
        count_SN_B += 1
        sn_responses.append(selection[17][1])
        nineteenth()
    else:
        print('Not valid dear :)! try again')
        eighteenth()


def nineteenth():
    global tf_responses
    global count_TF_A
    global count_TF_B
    query19 = input(selection[18][0] + ' \t' + selection[18][1])
    if query19.casefold() == 'a':
        count_TF_A += 1
        tf_responses.append(selection[18][0])
        twentieth()
    elif query19.casefold() == 'b':
        count_TF_B += 1
        tf_responses.append(selection[18][1])
        twentieth()
    else:
        print('Not valid dear :)! try again')
        nineteenth()


def twentieth():
    global jp_responses
    global count_JP_A
    global count_JP_B
    query20 = input(selection[19][0] + ' \t' + selection[19][1])
    if query20.casefold() == 'a' or query20.casefold() == 'b':
        count_JP_A += 1
        jp_responses.append(selection[19][0])
    else:
        count_JP_B += 1
        jp_responses.append(selection[19][1])
        print('Not valid dear :)! try again')
        twentieth()


def main():
    first()


main()

print('*' * 100)
name_responses.append(name)
for index in name_responses:
    print(f"\t\t\tHi {index}!!!")

print('*' * 100)
for index in ei_responses:
    print(index)
print(f"Total number of A chosen is {count_Ei_A}\nTotal number of B chosen is {count_Ei_B}\n{'*' * 100}")

print('*' * 100)
for index in sn_responses:
    print(index)
print(f"Total number of A chosen is {count_SN_A}\nTotal number of B chosen is {count_SN_B}\n{'*' * 100}")

print('*' * 100)
for index in tf_responses:
    print(index)
print(f"Total number of A chosen is {count_TF_A}\nTotal number of B chosen is {count_TF_B}\n{'*' * 100}")

print('*' * 100)
for index in jp_responses:
    print(index)
print(f"Total number of A chosen is {count_JP_A}\nTotal number of B chosen is {count_JP_B}\n{'*' * 100}")

print(f""" Personality types => 
        1. INFJ: 
        An Advocate INFJ is someone with the Introverted, Intuitive, Feeling, 
        and Judging personality traits. They tend to approach life with deep thoughtfulness and imagination. 
        Their inner vision personal values, and a quiet, principled version of humanism guide them in all things. 
        2. ENFP:
        ENFP is someone with the Extroverted, Intuitive, Feeling, and Prospecting personality traits. 
        These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others. 
        Their vibrant energy can flow in many directions. 
        3. INFP: 
        INFP is someone who possesses the Introverted, Intuitive, Feeling, and Prospecting personality traits. 
        These rare personality types tend to be quiet, open-minded, and imaginative, 
        and they apply a caring and creative approach to everything they do. 
        4. INTP: 
        INTP is someone with the Introverted, Intuitive, Thinking, and Prospecting personality traits. 
        These flexible thinkers enjoy taking an unconventional approach to many aspects of life. 
        They often seek out unlikely paths, mixing willingness to experiment with personal creativity. 
        5. INTJ: 
        INTJ is a person with the Introverted, Intuitive, Thinking, and Judging personality traits. 
        These thoughtful tacticians love perfecting the details of life, 
        applying creativity and rationality to everything they do. 
        Their inner world is often a private, complex one. 
        6. ISFJ: 
        ISFJ is someone with the Introverted, Observant, Feeling, and Judging personality traits. 
        These people tend to be warm and unassuming in their own steady way. They’re efficient and responsible, 
        giving careful attention to practical details in their daily lives. 
        7. ISTJ: 
        A Logistician ISTJ is someone with the Introverted, Observant, Thinking, and Judging personality traits. 
        These people tend to be reserved yet willful, with a rational outlook on life. 
        They compose their actions carefully and carry them out with methodical purpose. 
        8. ISTP: 
        ISTP is someone with the Introverted, Observant, Thinking, and Prospecting personality traits. 
        They tend to have an individualistic mindset, pursuing goals without needing much external connection. 
        They engage in life with inquisitiveness and personal skill, varying their approach as needed. 
        9. ESFP: 
        ESFP is a person with the Extraverted, Observant, Feeling, and Prospecting personality traits. 
        These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown.
        They can be very social, often encouraging others into shared activities. 
        10. ESFJ: 
        ESFJ is a person with the Extraverted, Observant, Feeling, and Judging personality traits. 
        They are attentive and people-focused, and they enjoy taking part in their social community. 
        Their achievements are guided by decisive values, and they willingly offer guidance to others. 
        11. ESTJ: 
        ESTJ is someone with the Extraverted, Observant, Thinking, and Judging personality traits. 
        They possess great fortitude, emphatically following their own sensible judgment. 
        They often serve as a stabilizing force among others, able to offer solid direction amid adversity. 
        12. ESTP: 
        ESTP is someone with the Extraverted, Observant, Thinking, and Prospecting personality traits. 
        They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. 
        They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits. 
        13. ISFP: 
        ISFP is a person with the Introverted, Observant, Feeling, and Prospecting personality traits. 
        They tend to have open minds, approaching life, new experiences, and people with grounded warmth. 
        Their ability to stay in the moment helps them uncover exciting potentials.
        14. ENTP: 
        An ENTP is a person with the Extraverted, Intuitive, Thinking, and Prospecting personality traits. 
        They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. 
        They pursue their goals vigorously despite any resistance they might encounter. 
        15. ENTJ: 
        A ENTJ is someone with the Extraverted, Intuitive, Thinking, and Judging personality traits. 
        They are decisive people who love momentum and accomplishment. They gather information to construct 
        their creative visions but rarely hesitate for long before acting on them.
        16. ENFJ: 
        A  ENFJ is a person with the Extraverted, Intuitive, Feeling, and Judging personality traits. These warm, 
        forthright types love helping others, and they tend to have strong ideas and values. They back their perspective 
        with the creative energy to achieve their goals. """)

if count_Ei_A > count_Ei_B:
    personality_type.append('E')
else:
    personality_type.append('I')
if count_SN_A > count_SN_B:
    personality_type.append('S')
else:
    personality_type.append('N')
if count_TF_A > count_SN_B:
    personality_type.append('T')
else:
    personality_type.append('F')
if count_JP_A > count_JP_B:
    personality_type.append('J')
else:
    personality_type.append('P')
print('Your personality type is ->')
for items in personality_type:
    print(items, end='')
