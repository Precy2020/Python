def my_table(x=int(input())):
    for p in range(1, 13):
        print('\t')
        for y in range(1, x):
            print(f"{y:>3} x {p} = {y * p:<3}", end="\t\t")


my_table()


