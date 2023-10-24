def _is_arranged(word1, word2):
    if len(word1) == len(word2):
        for i in range(len(word1)):
            for j in word2:
                if word1[i] == j:
                    return True
                else:
                    return False


first_word = "Favour"
second_word = "avouFr"

print(_is_arranged(first_word, second_word))
