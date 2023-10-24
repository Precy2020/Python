def reverse_string(string: str):
    print(string[: - 1])
    for characters in range(len(string)):
        reverse = string[1 - characters]
        print(reverse)


print(reverse_string(input(">> ")))
