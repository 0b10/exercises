import unittest
from python.replace_with_alphabet_position.solution import alphabet_position


class ReplaceWithAlphabetPositionTestCase(unittest.TestCase):
    def test_can_run(self):
        alphabet_position("")

    def test_all_characters(self):
        """
        Test that lowercase alphabet characters [a-z] return 0-26, as positional values, relative to their
        position in the alphabet.
        """
        self.assertEqual(
            "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26",
            alphabet_position("abcdefghijklmnopqrstuvwxyz"),
            "Test for lowercase alphabet has returned incorrect values."
        )

    def test_uppercase(self):
        """
        Test that uppercase alphabet characters [A-Z] return 0-26, as positional values, relative to their
        position in the alphabet.
        """
        self.assertEqual(
            "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26",
            alphabet_position("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            "Test for uppercase alphabet has returned incorrect values."
        )

    def test_numbers_only(self):
        """
        Test that numbers only, will return an empty string.
        """
        self.assertEqual(
            "",
            alphabet_position("123456789"),
            "Test for numbers only has returned incorrect value."
        )

    def test_non_alphabetic_characters(self):
        """
        Test that non-alphabetic characters will return an empty string.
        """
        self.assertEqual(
            "",
            alphabet_position("-1-2-3-4-5"),
            "Non alphabetic characters should return an empty string."
        )

    def test_spaces_only(self):
        """
        Test that spaces only will return an empty string.
        """
        self.assertEqual(
            "",
            alphabet_position("       "),
            "Spaces only should return an empty string."
        )

    def test_alphabetic_characters_with_spaces(self):
        """
        Test that values are only returned for alphabetic characters.
        """
        self.assertEqual(
            "1 2 3 21 12 9 15 26",
            alphabet_position("a 1 2 b c * U l ; I O z"),
            "Values should only be returned from alphabetic characters."
        )

    def test_boundary(self):
        """
        Test the boundaries: [aAzZ].
        """
        self.assertEqual(
            "1 1 26 26",
            alphabet_position("a A z Z"),
            "Boundary values are 1 for a (and A) and 26 for z (and Z)."
        )

    def test_given_example(self):
        """
        Test the example given with the exercise.
        """
        self.assertEqual(
            "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
            alphabet_position("The sunset sets at twelve o' clock."),
            "Characters should return their positional values, relative to the alphabet"
        )

    def test_real_sentence(self):
        """
        This tests one of the test cases, given with the exercise. It tests a typical sentence.
        """
        self.assertEqual(
            "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20",
            alphabet_position("The narwhal bacons at midnight."),
            "Characters should return their positional values, relative to the alphabet"
        )


if __name__ == '__main__':
    unittest.main()

