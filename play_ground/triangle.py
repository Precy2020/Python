num = 6
for row in range(num + 1):
    for column in range(row, num):
        print(' ', end=' ')
    for column in range(row):
        print('*', end=' ')
    for column in range(row + 1):
        print('*', end=" ")
    print()
# for row in range(num):
#     for column in range(row + 1):
#         print(' ', end=' ')
#     for column in range(row, num - 1):
#         print('*', end=' ')
#     for column in range(row, num):
#         print('*', end=" ")
#     print()




