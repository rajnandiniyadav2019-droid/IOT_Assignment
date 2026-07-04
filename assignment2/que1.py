def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    return count


def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1

    return count


def vowel_consonant_ratio(s):
    vowels = count_vowels(s)
    consonants = count_consonants(s)

    if consonants == 0:
        return "Consonants count is zero"

    return vowels / consonants


string = input("Enter a string: ")

print("Vowels =", count_vowels(string))
print("Consonants =", count_consonants(string))
print("Ratio =", vowel_consonant_ratio(string))
