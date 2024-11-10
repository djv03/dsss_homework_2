import unittest
from math_quiz import getRandint, getRandoperation, doArithmetic


class TestMathGame(unittest.TestCase):

    def test_getRandint(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = getRandint(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_getRandoperation(self):
        # TODO
        for _ in range(1000):  # Test a large number of random values
            result = getRandoperation()
            self.assertIn(result, ['+', '-', '*'], f"Unexpected result: {result}")

    def test_doArithmetic(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),                
                (10, 4, '-', '10 - 4', 6),
                (3, 5, '*', '3 * 5', 15),
                (0, 5, '+', '0 + 5', 5),
                (5, 0, '-', '5 - 0', 5),
                (0, 5, '*', '0 * 5', 0),
                (-3, -4, '+', '-3 + -4', -7),
                (-10, 4, '-', '-10 - 4', -14),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                # Call the function with the current test case
                problem, result = doArithmetic(num1, num2, operator)
            
                # Check that the problem string matches the expected string
                self.assertEqual(problem, expected_problem, f"Expected problem: {expected_problem}, but got: {problem}")
            
                # Check that the result matches the expected answer
                self.assertEqual(result, expected_answer, f"Expected answer: {expected_answer}, but got: {result}")
                pass

if __name__ == "__main__":
    unittest.main()
