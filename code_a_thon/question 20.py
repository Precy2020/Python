# def big_list(num: int):
#     double = []
#     for i in range(num):
#         double.append(i * 2)
#     return double
#
#
# print(big_list(6))

def design(fn):
    print('=' * 100)
    fn()
    print('-' * 100)
    return fn


@design
def show():
    print("I am a Virtuous Lady!!!")
