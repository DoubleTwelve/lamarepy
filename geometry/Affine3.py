from ..geometry import np
import math


class Affine3(object):

    def __init__(self, R = np.eye(3),  t = [0, 0, 0]):
        self._coeffs = np.array([[R[0][0], R[0][1], R[0][2], t[0]],
                                 [R[1][0], R[1][1], R[1][2], t[1]],
                                 [R[2][0], R[2][1], R[2][2], t[2]],
                                 [0, 0, 0, 1]])

    def matrix(self):
        return self._coeffs

    def linear(self):
        return self._coeffs[0:3, 0:3]

    def translation(self):
        return self._coeffs[0:3, 3]