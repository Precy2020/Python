my_name = "Speciousness"
print(id(my_name))
my_names = my_name + ' ' + 'Precious'
print(id(my_names))

x = [1, 2, 3]
print(id(x))
x.append(5)
print(x)

name = 'ty'
last_name = name
together = name == last_name
print(together)
