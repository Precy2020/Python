# even = "even: "
# odd = "odd: "
#
# joy = int(input("Enter a number: "))
# for favour in range(joy, 0, -1):
#     if favour % 2 == 0:
#          even += str(favour) + " "
#     else:
#         odd+= str(favour) + " ")
# print(even)
# print(odd)


for number in range(joy, 0, -1):

    if number % 2 != 0:
        odd = number
        print(odd, end=" ")
print("\nEven")
for number in range(joy, 0, -1):
    if number % 2 == 0:
        even = number
        print(even, end=" ")