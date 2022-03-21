# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:04:40 2022

@author: quann
"""

#Bai 1 :
# numpy.apply_along_axis (1d_func, axis, array, args, kwargs)
  #  1d_func: hàm bắt buộc để thực hiện trên mảng 1D. Nó chỉ có thể được áp dụng trong các lát cắt 1D của mảng đầu vào và cả mảng đó dọc theo một trục cụ thể.
  #  trục   : trục bắt buộc dọc theo đó chúng tôi muốn mảng đầu vào được cắt
  #  mảng   : mảng đầu vào để làm việc
  #  args   : Đối số bổ sung cho 1D_func1d.
  #  kwargs : Các đối số bổ sung cho 1D_func1d.
#Returns
 #outndarray (Ni…, Nj…, Nk…)
 #Mảng đầu ra. Hình dạng của out giống với hình dạng của arr, ngoại trừ dọc theo chiều trục. Trục này bị loại bỏ và được thay thế bằng các kích thước mới bằng hình dạng của giá trị trả về của func1d. Vì vậy, nếu func1d trả về một đại lượng vô hướng sẽ có ít thứ nguyên hơn arr.
#Bai 2 :
import numpy as np
A = np.random.rand(15,17)
print (A)
#Bài 3 :
A1 = np.random.rand(3,4)
print(A1)
c = np.apply_along_axis(sorted, 1, A1)
print("Giá trị cuối cùng từng mảng là giá trị cao nhất của mỗi mảng đó ", c)
#Bài 4 :

#Bài 5 :
def arr_sum(arr):
    return np.sum(arr)
A2 = np.random.rand(3,4)
print(A2)
print(np.shape(A2))
e = np.apply_along_axis(arr_sum, 0, A2)
print("Tổng tất cả các phần tử của từng mảng là : " ,e)




    

