def slice_list(lists, step):
    return [lists[index::step] for index in range(step)]


sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(slice_list(sample, 3))
