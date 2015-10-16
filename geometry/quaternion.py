from ..geometry import np
import math

class quaternion(object):

    def __init__(self, coeffs=[0., 0., 0., 1.]):
        self._coeffs = np.array(coeffs)

    def vec(self):
        return self._coeffs[0:3]

    def coeffs(self):
        return self._coeffs

    def normalize(self):
        norm = np.linalg.norm(self._coeffs)
        self._coeffs = self._coeffs/norm

    def normalized(self):
        norm = np.linalg.norm(self._coeffs)
        coeffs = self._coeffs/norm
        return quaternion(coeffs)

    @property
    def w(self):
        return self._coeffs[3]

    @w.setter
    def w(self, value):
        self._coeffs[3] = value

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

    def conjugate(self):
        return quaternion([-self.x(), -self.y(), -self.z(), self.w()])

    def to_rotation_matrix(self):
        qx, qy, qz, qw = self._coeffs
        sqw = qw * qw
        sqx = qx * qx
        sqy = qy * qy
        sqz = qz * qz
        invs = 1. / (sqx + sqy + sqz + sqw)

        m00 = ( sqx - sqy - sqz + sqw) * invs
        m11 = (-sqx + sqy - sqz + sqw) * invs
        m22 = (-sqx - sqy + sqz + sqw) * invs

        qxy = qx * qy
        qzw = qw * qz

        m10 = 2. * (qxy + qzw) * invs
        m01 = 2. * (qxy - qzw) * invs

        qxz = qx * qz
        qyw = qy * qw

        m20 = 2.0 * (qxz - qyw) * invs
        m02 = 2.0 * (qxz + qyw) * invs

        qyz = qy * qz
        qxw = qx * qw

        m21 = 2. * (qyz + qxw) * invs
        m12 = 2. * (qyz - qxw) * invs

        return np.array([[m00, m01, m02], [m10, m11, m12], [m20, m21, m22]])

    @staticmethod
    def from_rotation_matrix(rotmat):
        m00, m01, m02 = rotmat[0]
        m10, m11, m12 = rotmat[1]
        m20, m21, m22 = rotmat[2]
        trace = m00 + m11 + m22

        if (trace > 0.):
            S = math.sqrt(trace + 1.0) * 2.
            qw = 0.25 * S
            qx = (m21 - m12) / S
            qy = (m02 - m20) / S
            qz = (m10 - m01) / S
            return quaternion([qx, qy, qz, qw])
        elif (m00 > m11 and m00 > m22):
            S = math.sqrt(1. + m00 - m11 - m22) * 2
            qw = (m21 - m12) / S
            qx = 0.25 * S
            qy = (m01 + m10) / S
            qz = (m02 + m20) / S
            return quaternion([qx, qy, qz, qw])
        elif (m11 > m22):
            S = math.sqrt(1.0 + m11 - m00 - m22) * 2
            qw = (m10 - m20) / S
            qx = (m01 + m10) / S
            qy = 0.25 * S
            qz = (m12 + m21) / S
            return quaternion([qx, qy, qz, qw])
        else:
            S = math.sqrt(1.0 + m22 - m00 - m11) * 2
            qw = (m10 - m01) / S
            qx = (m02 + m20) / S
            qy = (m12 + m21) / S
            qz = 0.25 * S
            return quaternion([qx, qy, qz, qw])












