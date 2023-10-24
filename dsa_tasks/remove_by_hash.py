def compare_strings_after_hash_removal(first_string1: str, second_string2: str):
    def remove_hashtag_and_previous_letter(input_string: str):
        results: list = []
        for i in range(len(input_string)):
            if input_string[i] == "#":
                i -= 1
            else:
                results.append(input_string[i])
        return ''.join(results)

    hash_free_string1 = remove_hashtag_and_previous_letter(first_string1)
    hash_free_string2 = remove_hashtag_and_previous_letter(second_string2)
    print(hash_free_string1)
    print(hash_free_string2)
    return len(hash_free_string1) == len(hash_free_string2)


string1: str = "a#b#d#pqrs#"
string2: str = "ac#d##pqr"
result = compare_strings_after_hash_removal(string1, string2)
print(result)

# def remove_hash(s: str, t: str):
#     def inputted(string: str):
#         new_list = [string]
#         for characters in new_list:
#             if characters == "#":
#                 characters -= 1
#                 new_list.remove(characters)
#
#     first_case = inputted("a#b#d#pqrs#")
#     second_case = inputted("ac#d##pqr")
