import unittest

def add(input):
    if (len(input) == 0):
        return 0
    if (',' not in input):
        return int(input)
    commapos=input.index(',')
    return int(input[:commapos])+int(input[commapos+1:])

class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        sum = add("")
        self.assertEqual(sum, 0)

    def test_one_number_returns_same(self):
        sum = add("1")
        self.assertEqual(sum, 1)

    def test_two_numbers_returns_sum(self):
        sum = add("5,2")
        self.assertEqual(sum, 7)

if __name__ == '__main__':
    unittest.main()

