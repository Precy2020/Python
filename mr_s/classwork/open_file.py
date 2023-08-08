# with open('account.txt', mode='w') as my_file:
#     print(my_file.write('001 Precious 22\n'))
#     print(my_file.write('002 Esther 20\n'))
#     print(my_file.write('003 Treasure 18\n'))
#     print(my_file.write('004 Praise 13\n'))
#     print(my_file.write('005 Anointed 11\n'))
#     my_file.close()

with open('account.txt', mode='r') as my_file:
    print(my_file.read())

