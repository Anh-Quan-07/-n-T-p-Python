# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:48:21 2022

@author: quann
"""

import numpy as np
import random
import math


# Bài 1:
A = np.array('[5, 7, 14]')
print(A)
print("dtype of matrix A: ", A.dtype)


# Bài 2:
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12],[13,14,15]])
print(B)
print("dtype of matrix :B", B.dtype)


# Bài 3:
n=int(input("Nhập 1 số nguyen dương n ="))
R = np.random.randn(n,1 )
print(R)


# Bài 4:
C  = np.array('[7,-5, 8]')
print (C)
D  = (7**2) + (5**2) + (8**2) 
print ("math.sqrt(B) : ", math.sqrt(D)) 


# Bài 5:
    
# Điểm A  :  
n = int(input("Nhập giới hạn 2 giá trị của điểm E = "))
E = np.random.randint(n,size=(1,2))
print(E)

# Điểm B : 
m = int(input("Nhập giới hạn 2 giá trị của điểm F = "))
F = np.random.randint(m,size=(1,2))
print(F)

# Tính Vecto EF :
G = E-F 
print (G)   

# Bài 6:
t1 = int(input("Nhập giới chiều dài của vecto 2 vecto   = "))

Q = np.random.randint(1000,size=(1,t1))

W = np.random.randint(1000,size=(1,t1))


# Tính tích vô hướng của vecto QW(O) :

T = np.inner(Q, W)
print (T)
    
    
# Bài 7:
t2 = int(input("Nhập giới chiều dài của vecto 2 vecto n  = "))

Z = np.random.randint(1000,size=(1,t2))


X = np.random.randint(1000,size=(1,t2))


# Tính tích vô hướng của vecto QW(O) :
V = np.inner(Z, X)
print (V)

# Tích hữu hướng
v3 = np.cross(Z,X)
print(v3) 

# Bài 8 :
t3 = int(input("Nhập giới chiều dài của vecto 2 vecto n  = "))

J = np.random.randint(1000,size=(1,t3))  

print ("Gía trị cua vecto a :" ,J )

# Ma trận chuyển vị : 
print(J.T)
print(np.transpose(J))

#Bài 9: 
a = [1, 2, 3, 4, 5]
b = [[1], [2], [3], [4], [5]]
print(a)
print(b)

#Bài 10:
m = input("nhập một số bât kỳ : ")
t4 = int(input("Nhập giới chiều dài của vecto 2 vecto n  = "))

Z1 = np.random.randint(1000,size=(1,t4))


X1 = np.random.randint(1000,size=(1,t4))
 
print (m,Z1)
print('Z1 + X1:', Z1 + X1)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


