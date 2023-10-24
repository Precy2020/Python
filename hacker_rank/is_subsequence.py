def subsequence(s: str, t: str):
    s_empty = []
    t_empty = []
    for character in range(len(s)):
        for characters in range(len(t)):
            if s[character] == t[characters]:
                s_empty.append(characters)
                t_empty.append(characters)

    s_empty.sort()
    return s_empty == t_empty


print(subsequence("abc", "abcde"))
