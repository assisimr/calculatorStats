import unittest

from Statistics.statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = (2, 4)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 3)

    def test_median_calculator(self):
        median= self.statistics.median(self.testData)
        self.assertEqual(median, 3)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, 4)

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.testData)
        self.assertEqual(variance, 1)

    def test_std_dev_calculator(self):
        std_div = self.statistics.std_dev(self.testData)
        self.assertEqual(std_div, 1)

if __name__ == '__main__':
    unittest.main()