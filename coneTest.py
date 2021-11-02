import unittest
import cone

class coneTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(cone.volume(10,32) == 3351.0321638291125)

    def test_volume2(self):
        assert(cone.volume(10,100) == 10471.975511965979)

    #failing test
    def test_volume3(self):
        assert(cone.volume(10,1000) == 0)


if __name__ == '__main__':
    unittest.main()