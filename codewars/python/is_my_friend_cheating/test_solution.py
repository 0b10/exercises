import unittest
from python.is_my_friend_cheating.solution import removNb


class MainTestCase(unittest.TestCase):
    def test_can_run(self):
        removNb(1)

    def test_given_example(self):
        """Test that all answers for the given example are valid."""
        n = 26
        sum_ = sum(range(1, n+1))
        for a, b in removNb(n):
            with self.subTest():
                self.assertEqual(
                    a * b,
                    sum_ - a - b,
                    "a*b must equal sum of 1..n, excluding a and b."
                )

    def test_n_is_1000(self):
        """Test that all answers up to 1000 are valid."""
        n = 1000

        self.assertEqual(
            removNb(n),
            [],
            "n = 1000 should return an empty list."
        )


if __name__ == '__main__':
    unittest.main()
