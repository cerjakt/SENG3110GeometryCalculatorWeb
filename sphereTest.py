import unittest
import sphere

class sphereTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(sphere.volume(32) == 137258.27743044044)

    def test_volume2(self):
        assert(sphere.volume(100) == 4188790.2047863905)

    #failing test
    def test_volume3(self):
        assert(sphere.volume(1000) == 0)

if __name__ == '__main__':
    unittest.main()