# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:10:20 2022

@author: quann
"""

import numpy as np
from numpy.linalg import inv
# Bài 1 :
A1 = np.random.randn(5, 7)
print(A1)

# Bài 2 :
A2 = np.zeros((6,7),dtype=int)
print(A2) 

# Bài 3 :
A3 = np.random.randn(7, 7)
print(A3)

# Bài 4 :
a = np.zeros((6, 6), int)
np.fill_diagonal(a, 15)
print (a)

# Bài 5 :
m = np.random.randn(8, 8)
print(np.triu(m,1))

# Bài 6 :
m1 = np.random.randn(8, 8)
print(np.triu(m1,-1))

# Bài 7 :
I = np.identity(9, dtype=np.float16)
print(I)

# Bài 8 :
A4 = np.random.randn(6, 7)
A5 = np.random.randn(6, 7)
A6 = A4 + A5 
print (A6)


A7 = np.random.randn(5, 8)
n=int(input("Nhập 1 số nguyen dương n ="))
K = A7 * n 
print (K)


A8 = np.random.randn(3, 7)
print("Ma trân gốc : \n", A8)
print("Ma trân chuyển vị: \n", A8.T)


A9 = np.random.randn(5, 7)
A10 = np.random.randn(7, 3)
D = np.dot(A9, A10)
print ( D)


A11  = np.random.randn(5, 5)
R = inv(np.matrix(A11))
print(R)


A12 = np.random.randn(1 , 8)
A13 = np.random.randn(8 , 1)
print (A12)
print (A13)

# Bài 10 :

import numpy as np
A14 = np.array([[4, 3, -5], 
              [-2, -4, 5], 
              [8, 8, 0]])

A15 = np.array([2, 5, -3])

x = np.linalg.solve(A14 , A15)

print(x)

#Giải các phương trình trên bằng cách sử dụng phương pháp nghịch đảo ma trận.
A_inv = np.linalg.inv(A14)

x = np.dot(A_inv, A15)
print(x)

from scipy.linalg import lu

P, L, U = lu(A14)
print('P:\n', P)
print('L:\n', L)
print('U:\n', U)
print('LU:\n',np.dot(L, U))
   # Kham khảo bải dựa trên 1 trang web 


























