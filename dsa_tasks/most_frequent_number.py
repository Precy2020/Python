# def frequent(lists):
#     new = 0
#     for n in range(len(lists)):
#         for number in range(len(lists)):
#             if lists[n] == lists[number]:
#                 new += 1
#         return n
#
#
# numbers = [4, 2, 2, 3]
# print(frequent(numbers))

def count_bs(string):
    count = 0
    for x in string:
        if x == "B":
            count += 1
    return count
      

strings = "BaBalola"
print(count_bs(strings))

counter = 0
for k in strings:
    if k == "B":
        counter += 1
print(counter)
