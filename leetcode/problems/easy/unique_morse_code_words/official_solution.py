"""
The official solution for the Unique Morse Code Words problem
https://leetcode.com/problems/unique-morse-code-words/solution/

Count the number of unique transformed morse code strings, given a sequence of words.
"""

'''
What I learned from this:
    * That ord(char) will return the unicode codepoint for char.
    * You can use `ord(char) - ord(a)` to create a lazy numerical character mapping for lists.
    * Essentially I learned that it's possible to map characters directly to array indices.
    * How to use nested comprehensions, and that they share the same scope.
    * Also that 'comprehensions', written inside of function(brackets) are actually generators. A list comprehension
        would have inner([square brackets]). A generator typically takes the form (foo), so this makes sense.
'''


class Solution(object):
    def __init__(self):
        self._morse = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--..")

    def uniqueMorseRepresentations(self, words):
        seen = {''.join(self._morse[ord(char) - ord('a')] for char in word) for word in words}
        return len(seen)


def test(s, words, expected_answer):
    assert s.uniqueMorseRepresentations(words) == expected_answer

solution = Solution()

test(solution, ["gin", "zen", "gig", "msg"], 2)
test(solution, ["a", "b", "c"], 3)
test(solution, ["df", "ba"], 2)
test(solution, ["du", "ba"], 1)
test(solution, ["tie", "b", "o", "ttt"], 2)
test(solution, ["e", "h"], 2)
test(solution, ["eeee", "h"], 1)