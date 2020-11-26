import numpy as np
import math

def compute_solution(M, V, P):
    m = np.matrix(M)
    sinTx = V[1]/math.sqrt(V[1]**2 + V[2]**2)
    cosTx = V[2]/math.sqrt(V[1]**2 + V[2]**2)

    sinTy = V[0]
    cosTy = math.sqrt(V[1]**2 + V[2]**2)

    #Transpunere
    T = ([1,0,0,P[0]], [0,1,0,P[1]], [0,0,1,P[2]], [0,0,0,1])

    #Rotx de -teta x
    RotXn = np.matrix([[1,0,0,0], [0, cosTx, sinTx, 0], [0, -sinTx, cosTx, 0], [0,0,0,1]])

    RotY = np.matrix([[cosTy, 0, sinTy, 0], [0, 1, 0, 0], [-sinTy, 0, cosTy, 0], [0,0,0,1]])

    Rxy = np.matrix([[1,0,0,0], [0,1,0,0], [0,0,-1,0], [0,0,0,1]])

    RotYn = np.matrix([[cosTy, 0, -sinTy, 0], [0, 1, 0, 0], [sinTy, 0, cosTy, 0], [0,0,0,1]])

    RotX = np.matrix([[1,0,0,0], [0, cosTx, -sinTx, 0], [0, sinTx, cosTx, 0], [0,0,0,1]])

    Tn = np.matrix([[1,0,0, -P[0]], [0,1,0, -P[1]], [0,0,1, -P[2]], [0,0,0,1]])

    #Product
    #m1 = T * RotXn
    #m2 = RotY * Rxy
    #m3 = RotYn * RotX

    #m4 = m1 * m2
    #m5 = m3 * Tn

    m6 = T * RotXn * RotY * Rxy * RotYn * RotX * Tn

    print(m6 * m)

def user_input():

    #Read the coordinates of the points of the polyhedron
    nr = int(input("How many points does the polyhedron have? "))
    x = []
    y = []
    z = []
    for i in range(nr):
        x1 = int(input("What is the x coordinate of this point? "))
        y1 = int(input("What is the y coordinate of this point? "))
        z1 = int(input("What is the z coordinate of this point? "))
        print()
        x.append(x1)
        y.append(y1)
        z.append(z1)

    #Read the parameters of the plane
    #print("Please enter the parameters of the plane:")
    #xp = int(input("X parameter: "))
    #yp = int(input("Y parameter: "))
    #zp = int(input("Z parameter: "))
    #xx = int(input("Free term: "))

    cX = []
    cY = []
    cZ = []
    print("Please enter 3 points from the plane:")
    for i in range(3):
        xp = int(input("X parameter: "))
        cX.append(xp)
        yp = int(input("Y parameter: "))
        cY.append(yp)
        zp = int(input("Z parameter: "))
        cZ.append(zp)
        print()

    #Compute the matrix
    last_line = []
    for i in range(nr):
        last_line.append(1)
    M = [x,y,z,last_line]

    #Normal Versor
    #residual = float("{:.2f}".format(math.sqrt(xp**2 + yp**2 + zp**2)))
    #x = float("{:.2f}".format(xp/residual))
    #y = float("{:.2f}".format(yp/residual))
    #z = float("{:.2f}".format(zp/residual))
    #V = [x, y, z]
    
    p1 = np.array([cX[0],cY[0], cZ[0]])
    p2 = np.array([cX[1],cY[1], cZ[1]])
    p3 = np.array([cX[2],cY[2], cZ[2]])

    v1 = p3-p1
    v2 = p2-p1
    cp = np.cross(v1,v2)
    a = cp[0]
    b = cp[1]
    c = cp[2]
    print(a)
    residual = math.sqrt(a**2 + b**2 + c**2)
    x = a/residual
    y = b/residual
    z = c/residual
    V = [x,y,z]

    #Point on plane
    P = [cX[0], cY[0], cZ[0]]

    #P = [0,0,0]
    #if (xp == 0 and yp == 0):
    #    P[2] = float("{:.2f}".format(-xx/zp))
    #elif (xp == 0 and zp == 0):
    #    p[1] = float("{:.2f}".format(-xx/yp))
    #elif (yp == 0 and zp == 0):
    #    p[0] = float("{:.2f}".format(-xx/xp))
    #elif(xp == 0):
    #    P[1] = float("{:.2f}".format(-xx/yp))
    #elif (yp == 0):
    #    P[0] = float("{:.2f}".format(-xx/xp))
    #elif (zp == 0):
    #    P[0] = float("{:.2f}".format(-xx/xp))
    return M, V, P


def print_menu():
    print("Welcome to the menu of this program!")
    print("This application will compute the image of the reflexion of any polyhedron on any given plane.")

def run():
    print_menu()
    M,V,P = user_input()
    compute_solution(M, V, P)

run()