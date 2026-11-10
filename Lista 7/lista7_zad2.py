def anagrams(word1, word2):
    w1 = ''.join(litera.lower() for litera in word1 if litera.isalpha())
    w2 = ''.join(ch.lower() for ch in word2 if ch.isalpha())

    return sorted(w1) == sorted(w2)

print(anagrams("Here come dots", "The morse code!"))