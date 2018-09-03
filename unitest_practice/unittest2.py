from unittest import TestCase

#create basic class, has one method, two arguments and returns a sum
class Calculator:
    def sum(self, a, b):
        return a + b


# a simple test case for this would be below

class TestCalculator(TestCase): ## test calculator is inhereting what the TestCase has
    def setUp(self):
        self.calc = Calculator()
    def test_sum(self):
        answer = self.calc.sum(2,4)
        self.assertEqual(answer,6)

#inheretence is a feature of OOP , allows object to have all properties(method/ attributes) of parent objects
        
