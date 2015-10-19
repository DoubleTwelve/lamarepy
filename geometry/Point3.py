from ..geometry import np

class Point3(object):

    def __init__(self, coeffs=[0., 0., 0.]):
        self._coeffs = np.array(coeffs[0:3])
        if (len(coeffs)==4):
            self._coeffs[0] /= coeffs[3]
            self._coeffs[1] /= coeffs[3]
            self._coeffs[2] /= coeffs[3]

    @property
    def x(self):
        return self._coeffs[0]

    @x.setter
    def x(self, value):
        self._coeffs[0] = value

    @property
    def y(self):
        return self._coeffs[1]

    @y.setter
    def y(self, value):
        self._coeffs[1] = value

    @property
    def z(self):
        return self._coeffs[2]

    @z.setter
    def z(self, value):
        self._coeffs[2] = value

    def coeffs(self):
        return self._coeffs

    def to_homogeneous(self):
        return np.array([self.x, self.y, self.z, 1.0])