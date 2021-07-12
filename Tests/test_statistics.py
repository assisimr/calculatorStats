import unittest

from Statistics.statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = (2, 4, 6, 8)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 5)

    def test_median_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 5)

if __name__ == '__main__':
    unittest.main()