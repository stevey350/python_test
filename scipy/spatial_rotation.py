import numpy as np
from math import *
from scipy.spatial.transform import Rotation as R

'''
Rotation实例可以以任何格式初始化, 并转换为任何其他格式(中间量)
生成Rotation对象, 采用方法from_quat, from_matrix, from_euler
转换输出采用方法as_quat, as_matrix, as_euler
'''

def Rot(alpha, beta, gamma):
    '''
    全局坐标系{g}沿着x-, y-, z-轴依次旋转alpha, beta, gamma角度得到磁铁坐标系{m}
    R_gm = Rx(alpha)*Ry(beta)*Rz(gamma)
    '''
    rot_x = np.array([[1, 0, 0],
                      [0, cos(alpha), -sin(alpha)],
                      [0, sin(alpha), cos(alpha)]])
    
    rot_y = np.array([[cos(beta), 0, sin(beta)],
                      [0, 1, 0],
                      [-sin(beta), 0, cos(beta)]])

    rot_z = np.array([[cos(gamma), -sin(gamma), 0],
                      [sin(gamma), cos(gamma), 0],
                      [0, 0, 1]])

    return rot_x.dot(rot_y.dot(rot_z))


# 绕z轴逆时针旋转90度
# 生成Rotation实例
R1 = R.from_quat([0, 0, np.sin(np.pi/4), np.cos(np.pi/4)])
R2 = R.from_matrix([[0, -1, 0],
                    [1, 0, 0],
                    [0, 0, 1]])
R3 = R.from_rotvec(np.pi/2 * np.array([0, 0, 1]))
R4 = R.from_euler('z', 90, degrees=True)

# 转换其它形式
print('quat: \n', R1.as_quat())
print('matrix: \n', R1.as_matrix())
print('rotvec: \n', R1.as_rotvec())
print('euler: \n', R1.as_euler('xyz', degrees=True))

'''
from_euler比较复杂
scipy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.from_euler.html
https://en.wikipedia.org/wiki/Euler_angles#Definition_by_intrinsic_rotations
intrinsic rotations: {'X', 'Y', 'Z'}  绕旋转之后的轴旋转
extrinsic rotations: {'x', 'y', 'z'}  绕固定坐标系旋转
'''


#----测试--------------------------------------------------------------------
theta = [pi/3, pi/4, pi/6]
R2 = R.from_euler('XYZ', theta, degrees=False)
R_gm = Rot(theta[0], theta[1], theta[2])

quat = R2.as_quat()
R3 = R.from_quat(quat)

print(R2.as_matrix())
print(R_gm)
print(R3.as_euler('XYZ'))       # [pi/3, pi/4, pi/6] = [1.04719755 0.78539816 0.52359878]