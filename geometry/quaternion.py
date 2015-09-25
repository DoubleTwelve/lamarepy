from ..geometry import np

class quaternion:

    def __init__(self, coeffs=[0., 0., 0., 1.]):
        self._coeffs = np.array([coeffs])

    def vec(self):
        return self._coeffs[0:3]

    def coeffs(self):
        return self._coeffs

    def normalize(self):
        norm = np.linalg.norm(self._coeffs)
        self._coeffs = self._coeffs/norm

    def w(self):
        return self._coeffs[3]

    def x(self):
        return self._coeffs[0]

    def y(self):
        return self._coeffs[1]

    def z(self):
        return self._coeffs[2]

    def conjugate(self):
        return quaternion([-self.x(), -self.y(), -self.z(), self.w()])



