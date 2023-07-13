weight1, price1 = input('Enter weight and price for package 1: ').split(" ", 1)
weight_i = float(weight1)
price_i = float(price1)
weight2, price2 = input('Enter weight and price for package 2: ').split(" ", 1)
weight_ii = float(weight2)
price_ii = float(price2)

first_package = weight_i / price_i
second_package = weight_ii / price_ii

if first_package > second_package:
    print('Package 1 has a better price')
else:
    print('Package 2 has a better price')

