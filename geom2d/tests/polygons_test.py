import unittest
from geom2d.polygon import Polygon
from geom2d.point import Point
from geom2d.polygons import make_polygon_from_coords

class TestPolygons(unittest.TestCase):

    def test_make_polygon(self):
        coords = [0,1,2,3,4,5]
        actual = make_polygon_from_coords(coords)
        expected = Polygon([Point(0,1), Point(2,3), Point(4,5)])
        self.assertEqual(actual, expected)

