import unittest
import primeNeighbor as pn

class PrimeNeighborTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test010(self):
        actualResult = pn.primeNeighbor(val=20)
        expectedResult = 19
        self.assertEqual(expectedResult, actualResult)

if  __name__ == '_main_':
    unittest.main()

