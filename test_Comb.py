import sys
import unittest
from Comb import *

sys.path.append(r'.\Comb.py')

class TestComb(unittest.TestCase):

    def test_calc(self):
        combtest = Comb('123', 3)
        count = combtest.calc()
        self.assertEqual(count,6)

if __name__ == '__main__':
    unittest.main()