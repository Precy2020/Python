# for love in range(len(my_list)):
#     for joy in range(my_list):
#         if my_list[love] < my_list[joy]:
#             my_list[love], my_list[joy] = my_list[joy], my_list[love]
#             print(my_list.append(my_list))

lister = [8, 2, 1, 5, 3, 9, 4, 6, 7]
joy = []
for index in range(len(lister)):
    joy.append(min(lister))
    lister.remove(min(lister))
print(joy)

