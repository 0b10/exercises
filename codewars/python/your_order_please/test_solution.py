import unittest
from python.your_order_please.solution import order


class YourOrderPleaseTestCase(unittest.TestCase):
    def test_can_run(self):
        order("")

    def test_basic_example(self):
        """This tests with the example provided."""
        self.assertEqual(
            order("is2 Thi1s T4est 3a"),
            "Thi1s is2 3a T4est",
            "Resultant string is not ordered correctly.\n"
        )

    def test_empty_string(self):
        """This tests for an empty string, which should return an empty string."""
        self.assertEqual(
            order(""),
            "",
            "Resultant string is not ordered correctly."
        )

    def test_for_zero(self):
        """
        This tests for situation where a word has a zero present, which should throw an IndexError exception,
        because the regex ignores 0, and ordering is based on the pattern found.  Sorted will not know where to put the
        item in the list.
        """
        self.assertRaises(
            AttributeError,
            order,
            "second1 first0",
        )

    def test_for_negation(self):
        """This tests for the negation symbol. This should be ignored."""
        self.assertEqual(
            order("second-2 first-1"),
            "first-1 second-2",
            "Resultant string is not ordered correctly."
        )

    def test_for_leading_zeros(self):
        """This tests for leading zeros. This should be treated as if they were truncated."""
        self.assertEqual(
            order("second2 first0001"),
            "first0001 second2",
            "Resultant string is not ordered correctly."
        )

    def test_for_prefixed_number(self):
        """This tests for words beginning with a number. This should obey the ordering rules."""
        self.assertEqual(
            order("second2 first1"),
            "first1 second2",
            "Resultant string is not ordered correctly."
        )

    def test_for_underscores(self):
        """This tests for an underscore separator. The string should be returned untouched."""
        self.assertEqual(
            order("second2_first1"),
            "second2_first1",
            "Resultant string is not ordered correctly."
        )

    def test_for_multiple_numbers_per_word(self):
        """This tests for multiple numbers in a word. For each word, nly the first number should be considered."""
        self.assertEqual(
            order("second2 1first3"),
            "1first3 second2",
            "Resultant string is not ordered correctly."
        )

    def test_all_numbers(self):
        """Test without characters, numbers only. This should still obey ordering rules"""
        self.assertEqual(
            order("2222 1111"),
            "1111 2222",
            "Resultant string is not ordered correctly."
        )

    def test_floats(self):
        """This tests for floats, and should still obey the ordering rules."""
        self.assertEqual(
            order("second1.2 first1.1"),
            "first1.1 second1.2",
            "Resultant string is not ordered correctly."
        )


if __name__ == '__main__':
    unittest.main()