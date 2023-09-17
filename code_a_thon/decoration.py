# def big_list(num: int):
#     double = []
#     for i in range(num):
#         double.append(i * 2)
#     return double
#
#
# print(big_list(6))

def design(fn):
    print('><' * 50)
    print('*' * 100)
    print('><' * 50)
    fn()
    print('><' * 50)
    print('*' * 100)
    print('><' * 50)
    return fn


