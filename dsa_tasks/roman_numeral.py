def roman_numeral(string: str):
    empty_list = []
    empty_variable = 0
    for characters in string:
        if characters.casefold() == "I".casefold():
            empty_list.append(1)
        if characters.casefold() == "V".casefold():
            empty_list.append(5)
        if characters.casefold() == "X".casefold():
            empty_list.append(10)
        if characters.casefold() == "L".casefold():
            empty_list.append(50)
        if characters.casefold() == "C".casefold():
            empty_list.append(100)
        if characters.casefold() == "D".casefold():
            empty_list.append(500)
        if characters.casefold() == "M".casefold():
            empty_list.append(1000)

    for numbers in range(len(empty_list)):
        if empty_list[0] < empty_list[numbers]:
            empty_variable = empty_list[numbers] - empty_variable
        else:
            empty_variable = empty_list[numbers] + empty_variable

    return empty_variable


print(roman_numeral("lviii"))
