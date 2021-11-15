from geom2d.point import Point
from geom2d.size import Size
from geom2d.polygon import Polygon
from geom2d.open_interval import OpenInterval

class Rect:
    def __init__(self, origin: Point, size: Size):
        self.origin = origin
        self.size = size

    def __horizontal_overlap_with(self, other):
        self_interval = OpenInterval(self.left, self.right)
        other_interval = OpenInterval(other.left, other.right)

        return self_interval.compute_overlap_with(other_interval)

    def __vertival_overlap_with(self, other):
        self_interval = OpenInterval(self.bottom, self.top)
        other_interval = OpenInterval(other.bottom, other.top)

        return self_interval.compute_overlap_with(other_interval)

    @property
    def left(self):
        return self.origin.x

    @property
    def right(self):
        return self.origin.x + self.size.width

    @property
    def bottom(self):
        return self.origin.y

    @property
    def top(self):
        return self.origin.y + self.size.height

    @property
    def area(self):
        return self.size.width * self.size.height

    @property
    def perimeter(self):
        return 2 * self.size.width + 2 * self.size.height

    def contains_point(self, point: Point):
        return self.left < point.x < self.right \
            and self.bottom < point.y < self.top

    def intersection_with(self, other):
        h_overlap = self.__horizontal_overlap_with(other)
        if h_overlap is None:
            return None

        v_overlap = self.__vertical_overlap_with(other)
        if v_overlap is None:
            return None

        return Rect(
            Point(h_overlap.start, v_overlap.start),
            Size(h_overlap.length, v_overlap.length)
        )

    def to_polygon(self):
        """
        Creates a `Polygon` equivalent to this rectangle.
        The polygon is made of the rectangle vertices in the
        following order:
            - (left, bottom) ≡ origin
            - (right, bottom)
            - (right, top)
            - (left, top)
        :return: `Polygon`
        """
        return Polygon([
            self.origin,
            Point(self.right, self.bottom),
            Point(self.right, self.top),
            Point(self.left, self.top)
        ])

    def __eq__(self, other):
        """
        Two rects are equal if their origins and sizes are equal.
        :param other: `Rect`
        :return: are the rects equal?
        """
        if self is other:
            return True

        if not isinstance(other, Rect):
            return False

        return self.origin == other.origin \
               and self.size == other.size   

