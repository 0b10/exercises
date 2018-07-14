import unittest
from python.tribonacci_sequence import solution


class TribonacciSequenceTestCase(unittest.TestCase):
    def test_can_run(self):
        """Determine if the function can run. This should return True."""
        solution.tribonacci([0, 0, 0], 0)

    def test_boundary_one(self):
        """Test for a list of [1, 1, 1], where n is 10"""
        self.assertEqual(
            solution.tribonacci([1, 1, 1], 10),
            [1, 1, 1, 3, 5, 9, 17, 31, 57, 105],
            "Invalid return."
        )

    def test_boundary_two(self):
        """Test for a list of [0, 1, 1], where n is 10"""
        self.assertEqual(
            solution.tribonacci([0, 1, 1], 10),
            [0, 1, 1, 2, 4, 7, 13, 24, 44, 81],
            "Invalid return."
        )

    def test_boundary_three(self):
        """Test for a list of [1, 0, 0], where n is 10"""
        self.assertEqual(
            solution.tribonacci([1, 0, 0], 10),
            [1, 0, 0, 1, 1, 2, 4, 7, 13, 24],
            "Invalid return."
        )

    def test_boundary_four(self):
        """Test for a list of [0, 0, 0], where n is 10"""
        self.assertEqual(
            solution.tribonacci([0, 0, 0], 10),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "Invalid return."
        )

    def test_boundary_five(self):
        """Test for a list of [0, 0, 1], where n is 10"""
        self.assertEqual(
            solution.tribonacci([0, 0, 1], 10),
            [0, 0, 1, 1, 2, 4, 7, 13, 24, 44],
            "Invalid return."
        )

    def test_one_two_three(self):
        """Test for a list of [1, 2, 3], where n is 10"""
        self.assertEqual(
            solution.tribonacci([1, 2, 3], 10),
            [1, 2, 3, 6, 11, 20, 37, 68, 125, 230],
            "Invalid return."
        )

    def test_three_two_one(self):
        """Test for a list of [3, 2, 1], where n is 10"""
        self.assertEqual(
            solution.tribonacci([3, 2, 1], 10),
            [3, 2, 1, 6, 9, 16, 31, 56, 103, 190],
            "Invalid return."
        )

    def test_all_ones(self):
        """Test for a list of [1, 1, 1], where n is 1"""
        self.assertEqual(
            solution.tribonacci([1, 1, 1], 1),
            [1],
            "Invalid return."
        )

    def test_n_is_zero(self):
        """Test for a list of [300, 200, 100], where n is 0"""
        self.assertEqual(
            solution.tribonacci([300, 200, 100], 0),
            [],
            "Invalid return."
        )

    def test_for_float(self):
        """Test for a list of [0.5, 0.5, 0.5], where n is 30"""
        self.assertEqual(
            solution.tribonacci([0.5, 0.5, 0.5], 30),
            [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5,
             6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5,
             5600910.5, 10301680.5],
            "Invalid return."
        )

    def test_n_is_two(self):
        """Test for a list of [1, 2, 3], where n is 2"""
        self.assertEqual(
            solution.tribonacci([1, 2, 3], 2),
            [1, 2],
            "Invalid return."
        )

    def test_n_is_three(self):
        """Test for a list of [1, 2, 3], where n is 3"""
        self.assertEqual(
            solution.tribonacci([1, 2, 3], 3),
            [1, 2, 3],
            "Invalid return."
        )

    def test_n_is_four(self):
        """Test for a list of [1, 2, 3], where n is 4"""
        self.assertEqual(
            solution.tribonacci([1, 2, 3], 4),
            [1, 2, 3, 6],
            "Invalid return."
        )


    '''
    Test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
    #Test.assert_equals(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
    #Test.assert_equals(tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
    #Test.assert_equals(tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    #Test.assert_equals(tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
    #Test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
    #Test.assert_equals(tribonacci([1, 1, 1], 1), [1])
    #Test.assert_equals(tribonacci([300, 200, 100], 0), [])
    #Test.assert_equals(tribonacci([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5,
    326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5,
    900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5])
    '''


if __name__ == '__main__':
    unittest.main()