"""WRITE A PYTHON PROGRAM TO TEST WHETHER A PASSED LETTER IS A VOWEL OR NOT"""


def vowel_validator(letter):
    vowel = ['a', 'e', 'i', 'o', 'u']
    empty = []

    for letters in vowel:
        if letter == letters:
            return "Vowel"
        else:
            return "Not vowel"


print(vowel_validator('a'))
