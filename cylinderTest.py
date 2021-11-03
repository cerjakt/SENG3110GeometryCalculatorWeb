import unittest
import cylinder

class cylinderTest(unittest.TestCase):

    #passing tests
    def test_surfacearea(self):
        assert(cylinder.surfArea(10, 32) == 2638.94)

    def test_volume(self):
        assert(cylinder.volume(10, 32) == 10053.1)

    def test_lateralsurfacearea(self):
        assert(cylinder.latSurfArea(10, 32) == 2010.62)

    def test_topbotsurfacearea(self):
        assert(cylinder.topBotArea(10, 32) == 314.16)

if __name__ == '__main__':
    unittest.main()