import numpy as np

def array():
    array1 = np.array([-2.33,100,20,33.2])
    array2 = np.array([[30,12,2,70.2],[98.01,4,0,7]])
    array3 = np.arange(2,12,2)
    array4 = np.arange(20,-30,-10)
    array5 = np.linspace(0,1,4)
    array6 = np.ones((3,4))
    array7 = np.zeros((2,3))
    array8 = np.eye(3)
    array9 = np.diag(np.ones((2,)),-1)
    array10 = np.array([np.zeros((4,)), np.ones((4,)), 2*np.ones((4,))])
    return array1,array2,array3,array4,array5,array6,array7,array8,array9,array10


def total_displacement(v1x,v1y,v2x,v2y,v3x,v3y):
    v1 = np.array([v1x,v1y])
    v2 = np.array([v2x,v2y])
    v3 = np.array([v3x,v3y])
    vR = v1 + v2 + v3
    u = np.array([1/np.sqrt(2),-1/np.sqrt(2)])
    vRu = np.dot(vR,4)*u
    len_vRu = np.sqrt(vRu[0]**2 + vRu[1]**2)
    return vR,len_vRu
