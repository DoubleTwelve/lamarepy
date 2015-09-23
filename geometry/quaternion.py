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
