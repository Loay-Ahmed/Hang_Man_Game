"""Hang Man Game"""

import random

words = ["ant", "cat", "woman", "man", "dog", "snake", "elephant", "giraffe", "ostrich",
         "monkey", "rhino", "hippo", "chipmunk"]

# diferent stages for wrong guess
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


def text(wrd):
    """Hiding the characters of the word"""

    txt = "_ "
    txt *= len(wrd)
    return txt


def main():
    print(text(word))
    """ The main function that combines all the other functions """
