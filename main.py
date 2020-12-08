import mecode
import turtle
import math


def check_is_type(obj, *types):
    for type in types:
        if type is None:
            if obj is type:
                return
            continue
        elif isinstance(obj, type):
            return
    types = ', '.join([type.__name__ for type in types])
    raise TypeError(f"{repr(obj)} is not one of these types, {types}")


def rad_to_deg(rad):
    return rad / math.pi * 180


def deg_to_rad(deg):
    return deg / 180 * math.pi


class G2(mecode.G):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._xy_angle = 0
        self._z_angle = 0

    def forward(self, distance):
        check_is_type(distance, int, float)
        self.move(
            distance * math.cos(deg_to_rad(self._xy_angle)),
            distance * math.sin(deg_to_rad(self._xy_angle)),
            distance * math.sin(deg_to_rad(self._z_angle))
        )

    def turn_degrees(self, xy_theta=None, z_theta=None):
        check_is_type(xy_theta, None, int, float)
        check_is_type(z_theta, None, int, float)
        if xy_theta:
            self._xy_angle += xy_theta
        if z_theta:
            self._z_angle += z_theta

    def turn_to(self, xy_theta=None, z_theta=None):
        check_is_type(xy_theta, None, int, float)
        check_is_type(z_theta, None, int, float)
        if xy_theta:
            self._xy_angle = xy_theta
        if z_theta:
            self._z_angle = z_theta

    def circle(self, radius):
        pass

    def sphere(self, radius):
        pass


g = G2(outfile='sphere.gcode')

g.view()
