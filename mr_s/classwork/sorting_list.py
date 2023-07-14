# for love in range(len(my_list)):
#     for joy in range(my_list):
#         if my_list[love] < my_list[joy]:
#             my_list[love], my_list[joy] = my_list[joy], my_list[love]
#             print(my_list.append(my_list))

love = [8, 2, 1, 5, 3, 9, 4, 6, 7]
joy = []
for peace in range(len(love)):
    joy.append(min(love))
    love.remove(min(love))
print(joy)
