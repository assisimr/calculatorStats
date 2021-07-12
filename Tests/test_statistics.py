import unittest

from Statistics.mode import mode
from Statistics.median import median
from Statistics.statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = (2, 4, 4)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 3.3333333333333335)

    def test_median_calculator(self):
        median= self.statistics.median(self.testData)
        self.assertEqual(median, 0.6666666666666666)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, 4)

if __name__ == '__main__':
    unittest.main()