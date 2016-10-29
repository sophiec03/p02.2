"""
Problem:

    Suzy Dent is having trouble finding words in the dictionary.
    To help her, we are going to write a function that will tell
    us whether a word is before or after another word so she
    knows whether to go forward or backwards.

    The function 'dictionary' takes two words. If the first word
    is before the other in the dictionary, print "Go back!".
    If the first word is after the other in the dictionary, print
    "Keep going".  If they are the same, print "You're there!".

    The words could be upper or lower case, but this should not
    affect the outcome. It should be case-insensitive.

Tests:

    >>> dictionary("Apple", "Banana")
    Go back!
    >>> dictionary("Pineapple", "peach")
    Keep going
    >>> dictionary("lemon", "lime")
    Go back!
    >>> dictionary("grape", "Plum")
    Go back!
    >>> dictionary("Orange", "nectarine")
    Keep going
    >>> dictionary("Grapefruit", "grapefruit")
    You're there!

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def dictionary(word1, word2):
    
     if word1 == word2:
        print("You're there!")

    elif word1.lower() == word2.lower():
        print("You're there!")

    elif word1.upper() == word2.upper():
        print("You're there!")

    elif word1 <= word2:
        print("Go back")

    elif word1 >= word2:
        print("Go back")

    
    else:
        print("Keep going")
