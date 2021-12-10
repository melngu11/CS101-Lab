import unittest
import Grades
import math

class Grade_test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result, 33,'The total function should return 33')
    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result, 0,'The total function should return 0')
    def test_average_one(self):
        result = Grades.average([2,5,9])
        self.assertAlmostEqual( 0.1 + 0.2, 0.3, 3) 
    def test_average_two(self):
        result = Grades.average([2,15,22,9])
        self.assertAlmostEqual(result,12.0000,4)
    def test_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs(result,math.nan)  
    def test_median_one(self):
        result = Grades.median([2,5,1])
        self.assertEqual(result, 2,'The total function should return 2')
    def test_median_two(self):
        result = Grades.median([5,2,1,3])
        self.assertEqual(result, 2.5,'The total function should return 2.5')
    def test_median_error(self):
        with self.assertRaises(ValueError):
            result = Grades.median([])
unittest.main()


