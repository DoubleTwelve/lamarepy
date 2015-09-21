class Quaternion:
    __coeffs = np.array([0., 0., 0., 1.])


    def vec(self):
        return self.__coeffs[0:3]

    def coeffs(self):
        return self.__coeffs

    def normalize(self):
        norm = np.linalg.norm(self.__coeffs)
        self.__coeffs = self.__coeffs/norm
