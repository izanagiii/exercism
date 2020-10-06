from string import ascii_lowercase

# Solu izanagiii
def is_pangram(sentence):
    sentence_lower = sentence.lower()
    for letter in ascii_lowercase:
        if letter not in sentence_lower:
            return False
    else:
        return True

# print(is_pangram("the lazy dog jumps over the quick brown fox"))