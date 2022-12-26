"""Hang Man Game"""

import random

with open("words.txt", "r") as file:
    words = (file.read()).split(" ")

# different stages for wrong guess
hangman = ["""
  ______
 |
 |
 |
 |
_|__""",
           """
  ______
 |      |
 |      O
 |
 |
_|__""",
           """
  ______
 |      |
 |      O
 |     /|
 |
_|__""",
           """
  ______
 |      |
 |      O
 |     /|\\
 |
_|__""",
           """
  ______
 |      |
 |      O
 |     /|\\
 |     /
_|__""",
           """
  ______
 |      |
 |      O
 |     /|\\
 |     / \\
_|__"""
           ]

# random choice from the words[]
word = random.choice(words)
txt = ['_'] * len(word)
indexes = []
i = 0

while i <= 5:
    print(" ".join(txt))
    letter = input("Enter a letter: ")

    while letter.isalpha() is False:
        letter = input("Enter a letter: ")

    if letter in word:
        indexes.clear()
        for (index, char) in enumerate(word):
            if char == letter:
                indexes.append(index)

        for index in indexes:
            txt[index] = letter
    else:
        i += 1
        for j in range(0, i):
            print(hangman[j])

    if word == "".join(txt):
        print("\n==>You WIN")
        break

if i > 5:
    print(f"Better Luck next time - the secret word is: {word}")
