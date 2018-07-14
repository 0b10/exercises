import unittest
from python.valid_parentheses import solution


class ValidParenthesesTestCase(unittest.TestCase):
    def test_can_run(self):
        """Test that the function can actually be run."""
        solution.valid_parentheses("test")

    def test_simple_open_and_close(self):
        """Test for a simple opening and closing of parentheses. This should return True."""
        self.assertTrue(
            solution.valid_parentheses("()"),
            "Opening and closing of brackets () should always be True"
        )

    def test_parens_only(self):
        """Test for parentheses only. This should return True."""
        self.assertTrue(
            solution.valid_parentheses("(())((()())())"),
            "A valid combination of parentheses should return True"
        )

    def test_single_left_paren(self):
        """Test for a single left parentheses. This should return False."""
        self.assertFalse(
            solution.valid_parentheses("("),
            "A single opening parentheses should always return False."
        )

    def test_invalid_combination(self):
        """Test for an invalid combination of parentheses. This should return False."""
        self.assertFalse(
            solution.valid_parentheses(")(()))"),
            "Opening with a right parentheses should always return False."
        )

    def test_for_closing_bracket_only(self):
        """Test for closing bracket only. This should return False."""
        self.assertFalse(
            solution.valid_parentheses(")"),
            "Opening with a right parentheses should always return False."
        )

    def test_for_empty_string(self):
        """Test an empty string. This should return True."""
        self.assertTrue(
            solution.valid_parentheses(""),
            "An empty string should return True."
        )

    def test_for_space_then_opening_bracket(self):
        """Test for a space, then an opening bracket. This should return False due to the bracket alone."""
        self.assertFalse(
            solution.valid_parentheses("  ("),
            "A single opening parentheses should return False, even when preceded with a space."
        )

    def test_for_closing_bracket_then_string(self):
        """Test for a closing bracket, then a string. This should return False due to the bracket alone."""
        self.assertFalse(
            solution.valid_parentheses(")test"),
            "A single closing bracket should return False, even with a following string."
        )

    def test_for_string_followed_by_valid_brackets(self):
        """Test for a string, followed by invalid brackets. The brackets alone should cause this to return False."""
        self.assertFalse(
            solution.valid_parentheses("hi())("),
            "An invalid sequence of brackets should always fail, even when preceded with a string."
        )

    def test_for_string_with_valid_brackets(self):
        """Test for a valid sequence of brackets, combined with other string characters. This should return True."""
        self.assertTrue(
            solution.valid_parentheses("hi(hi)()"),
            "A valid sequence of brackets should always return True, regardless of other strings."
        )


if __name__ == '__main__':
    unittest.main()


