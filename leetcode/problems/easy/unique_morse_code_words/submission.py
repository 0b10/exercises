import string

"""
Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words/description/

Count the number of unique transformed morse code strings, given a sequence of words.
"""

'''
A convenient list of morse code mappings:

A= .-       B= -...     C= -.-.     D= -..      E= .        F= ..-.     G= --.      H= ....
I= ..       J= .---     K= -.-      L= .-..     M= --       N= -.       O= ---      P= .--.
Q= --.-     R= .-.      S= ...      T= -        U= ..-      V= ...-     W= .--      X= -..-
Y= -.--     Z= --..

'''


class Solution:
    def __init__(self):
        morse_codes = (".-", "-...", "-.-.", "-..",
                       ".", "..-.", "--.", "....",
                       "..", ".---","-.-", ".-..",
                       "--", "-.", "---", ".--.",
                       "--.-", ".-.", "...", "-",
                       "..-", "...-", ".--", "-..-",
                       "-.--", "--..")
        alphabet = list(string.ascii_lowercase)
        self._morse_codes = dict(zip(alphabet, morse_codes))

        assert self._morse_codes['a'] == ".-"
        assert self._morse_codes['z'] == "--.."
        assert self._morse_codes['m'] == "--"

    def get_transformation(self, word):
        """
        Return a transformed string, given word.
        :param word: A string to be transformed.
        :return: A transformed string, in morse code form.
        """
        return ''.join([self._morse_codes[letter] for letter in word])

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str], a list of words to be transformed.
        :rtype: int, the number of unique transformed strings.
        """

        transformations = {self.get_transformation(word) for word in words}

        return len(transformations)


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

