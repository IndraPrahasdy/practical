"""
CP1404/CP5632 - Practical
Random word generator
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = "ccvcvvc"
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)