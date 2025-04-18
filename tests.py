import unittest
from utils import haversine

class TestGeoGuessr(unittest.TestCase):
    def test_haversine(self):
        # Test distance calculation between London and Paris
        self.assertAlmostEqual(haversine(51.5074, -0.1278, 48.8566, 2.3522), 343.4, delta=1.0)

if __name__ == '__main__':
    unittest.main()
