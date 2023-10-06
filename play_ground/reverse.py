# def reverse(strings):
#     return strings[:: -1]
#
#
# word = "wind", "air", "blow", "glory"
# print(reverse(word))

number = 67890.123

reversed_number_string = str(number)[::-1]
if type(number) == float:
    reversed_number = float(reversed_number_string)
elif type(number) == int:
    reversed_number = int(reversed_number_string)


print(reversed_number)
var = number[i - 1]
