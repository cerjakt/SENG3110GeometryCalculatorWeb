import unittest
import cone

class coneTest(unittest.TestCase):

    #passing tests
    def test_slant(self):
        assert(cone.slant(12, 25) == 27.73)

    def test_surfacearea(self):
        assert(cone.surfArea(12, 25) == 1497.82)

    def test_volume(self):
        assert(cone.volume(12, 25) == 3769.91)

    def test_lateralsurfacearea(self):
        assert(cone.latSurfArea(12, 25) == 1045.43)

if __name__ == '__main__':
    unittest.main()