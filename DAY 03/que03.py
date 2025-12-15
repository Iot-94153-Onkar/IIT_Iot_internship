def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count = count+ 1
    return count


def count_consonants(s):
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in "aeiouAEIOU":
             count = count+ 1
    return count


def vowel_consonant_ratio(s):
    vowels = count_vowels(s)
    consonants = count_consonants(s)

    if consonants == 0:
        return "Consonants count is zero, ratio cannot be calculated."

    ratio = vowels / consonants
    return ratio



text = input("Enter a string: ")

vowels = count_vowels(text)
consonants = count_consonants(text)
ratio = vowel_consonant_ratio(text)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Ratio of vowels to consonants:", ratio)
