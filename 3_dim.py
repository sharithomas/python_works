# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:32:33 2020

@author: SHARI
"""

#By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
import numpy as np
n1=3
n2=5
n3=8
multi_list=[[[0 for i in range (n3)] for j in range (n2)] for k in range(n1)]
array=np.array(multi_list)
print("dimension",array.ndim)
print("shape",array.shape)
print("array=\n",array)