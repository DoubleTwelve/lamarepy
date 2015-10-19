from ..geometry import Point3
from ..geometry import Affine3
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



def show_q(quat):
    R = quat.to_rotation_matrix()
    RT = Affine3(R)

    rot_point = lambda pt: Point3(np.inner(RT.matrix(), pt.to_homogeneous()))

    A = Point3([0, 0, 0.1])
    B = Point3([0, 5, 0.1])
    C = Point3([3, 5, 0.1])
    D = Point3([4, 4, 0.1])
    E = Point3([4, 3, 0.1])
    F = Point3([3.5, 2, 0.1])
    G = Point3([4, 1, 0.1])
    H = Point3([4, 0, 0.1])
    I = Point3([3, 0, 0.1])
    J = Point3([3, 1, 0.1])
    K = Point3([2, 2, 0.1])
    L = Point3([1, 2, 0.1])
    M = Point3([1, 0, 0.1])

    Ab = Point3([0, 0, -0.1])
    Bb = Point3([0, 5, -0.1])
    Cb = Point3([3, 5, -0.1])
    Db = Point3([4, 4, -0.1])
    Eb = Point3([4, 3, -0.1])
    Fb = Point3([3.5, 2, -0.1])
    Gb = Point3([4, 1, -0.1])
    Hb = Point3([4, 0, -0.1])
    Ib = Point3([3, 0, -0.1])
    Jb = Point3([3, 1, -0.1])
    Kb = Point3([2, 2, -0.1])
    Lb = Point3([1, 2, -0.1])
    Mb = Point3([1, 0, -0.1])


    A = rot_point(A)
    B = rot_point(B)
    C = rot_point(C)
    D = rot_point(D)
    E = rot_point(E)
    F = rot_point(F)
    G = rot_point(G)
    H = rot_point(H)
    I = rot_point(I)
    J = rot_point(J)
    K = rot_point(K)
    L = rot_point(L)
    M = rot_point(M)
    
    Ab = rot_point(Ab)
    Bb = rot_point(Bb)
    Cb = rot_point(Cb)
    Db = rot_point(Db)
    Eb = rot_point(Eb)
    Fb = rot_point(Fb)
    Gb = rot_point(Gb)
    Hb = rot_point(Hb)
    Ib = rot_point(Ib)
    Jb = rot_point(Jb)
    Kb = rot_point(Kb)
    Lb = rot_point(Lb)
    Mb = rot_point(Mb)


    X = [A.x, B.x, Bb.x, Ab.x, A.x,
         B.x, C.x, Cb.x, Bb.x, B.x,
         C.x, D.x, Db.x, Cb.x, C.x,
         D.x, E.x, Eb.x, Db.x, D.x,
         E.x, F.x, Fb.x, Eb.x, E.x,
         F.x, G.x, Gb.x, Fb.x, F.x,
         G.x, H.x, Hb.x, Gb.x, G.x,
         H.x, I.x, Ib.x, Hb.x, H.x,
         I.x, J.x, Jb.x, Ib.x, I.x,
         J.x, K.x, Kb.x, Jb.x, J.x,
         K.x, L.x, Lb.x, Kb.x, K.x,
         L.x, M.x, Mb.x, Lb.x, L.x,
         M.x, A.x, Ab.x, Mb.x, M.x]

    Y = [A.y, B.y, Bb.y, Ab.y, A.y,
         B.y, C.y, Cb.y, Bb.y, B.y,
         C.y, D.y, Db.y, Cb.y, C.y,
         D.y, E.y, Eb.y, Db.y, D.y,
         E.y, F.y, Fb.y, Eb.y, E.y,
         F.y, G.y, Gb.y, Fb.y, F.y,
         G.y, H.y, Hb.y, Gb.y, G.y,
         H.y, I.y, Ib.y, Hb.y, H.y,
         I.y, J.y, Jb.y, Ib.y, I.y,
         J.y, K.y, Kb.y, Jb.y, J.y,
         K.y, L.y, Lb.y, Kb.y, K.y,
         L.y, M.y, Mb.y, Lb.y, L.y,
         M.y, A.y, Ab.y, Mb.y, M.y]

    Z = [A.z, B.z, Bb.z, Ab.z, A.z,
         B.z, C.z, Cb.z, Bb.z, B.z,
         C.z, D.z, Db.z, Cb.z, C.z,
         D.z, E.z, Eb.z, Db.z, D.z,
         E.z, F.z, Fb.z, Eb.z, E.z,
         F.z, G.z, Gb.z, Fb.z, F.z,
         G.z, H.z, Hb.z, Gb.z, G.z,
         H.z, I.z, Ib.z, Hb.z, H.z,
         I.z, J.z, Jb.z, Ib.z, I.z,
         J.z, K.z, Kb.z, Jb.z, J.z,
         K.z, L.z, Lb.z, Kb.z, K.z,
         L.z, M.z, Mb.z, Lb.z, L.z,
         M.z, A.z, Ab.z, Mb.z, M.z]


    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")
    ax.plot(X, Y, Z)
    plt.show()
