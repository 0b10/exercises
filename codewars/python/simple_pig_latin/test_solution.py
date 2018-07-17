import unittest
from python.simple_pig_latin.solution import pig_it


class GeneralTestCase(unittest.TestCase):
    def test_can_run(self):
        pig_it("test")

    def test_single_word(self):
        """Test a single, simple word, with no punctuation."""
        self.assertEqual(
            "esttay",
            pig_it("test"),
            "First letter must be appended to the end each word, followed by 'ay'."
        )

    def test_two_words(self):
        """Test two, simple words, with no punctuation."""
        self.assertEqual(
            "esttay tringsay",
            pig_it("test string"),
            "First letter must be appended to the end each word, followed by 'ay'."
        )

    def test_trailing_punctuation(self):
        """Test several words with punctuation."""
        self.assertEqual(
            "esttay, esttay. esttay; esttay>",
            pig_it("test, test. test; test>"),
            "First letter must be appended to the end each word, followed by 'ay'. Punctuation, untouched."
        )

    def test_leading_punctuation(self):
        """Test a single, simple word."""
        self.assertEqual(
            ",esttay .esttay ;esttay <esttay",
            pig_it(",test .test ;test <test"),
            "First letter must be appended to the end each word, followed by 'ay'. Punctuation, untouched."
        )

    def test_edge_case(self):
        """Test a quite complex edge case."""
        self.assertEqual(
            "Oay elloHay-orldWay anmay! aay'yay?",
            pig_it("O Hello-World man! a'y?"),
            "First letter must be appended to the end each word, followed by 'ay'. Punctuation, untouched."
        )


if __name__ == '__main__':
    unittest.main()