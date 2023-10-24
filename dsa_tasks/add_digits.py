# def add(string: str):
# special_characters = "!@#$%^&*()-+?_=,<>/"
# empty_list = []
# temporary_variable = 0
# another_empty_variable = 0
# for special in special_characters:
#     print(special)
#         for character in string:
#             if character.isdigit() and character in special:
#                 empty_list.append(int(character))
#             else:
#                 return "null"
#         for numbers in empty_list:
#             temporary_variable += numbers
#         empty_variable = str(temporary_variable)
#
#         for num in empty_variable:
#             another_empty_variable += int(num)
#         return another_empty_variable
#
#
# print(add(input("Enter digits: ")))

string = "silent"
print(string[2] + string[1] + string[0])
