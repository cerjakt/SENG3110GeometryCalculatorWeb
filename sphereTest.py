import unittest
import sphere

class sphereTest(unittest.TestCase):

    #passing tests
    def test_volume(self):
        assert(sphere.volume(50) == 523598.78)

    def test_surfacearea(self):
        assert(sphere.surfArea(50) == 31415.93)

if __name__ == '__main__':
    unittest.main()