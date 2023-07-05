for x in range(1, 13):
    print('\t')
    for p in range(1, 13):
        print(f"{x:>3} x {p} = {x * p:<3}",  end="\t\t\t")
