import cv2
import numpy as np
import random
#==========================================================
# NumPy learning
#==========================================================
row1 = [1, 2, 3]
arr1 = np.array(row1, ndmin=2)
print(f"dimension = {arr1.ndim}")
print(f"shape = {arr1.shape}")
print(f"size = {arr1.size}")
print(f"array = {arr1}")
print("-"*70)
row2 = [4, 5, 6]
arr2 = np.array([row1,row2], ndmin=2)
print(f"dimension = {arr2.ndim}")
print(f"shape = {arr2.shape}")
print(f"size = {arr2.size}")
print(f"array = {arr2}")

#================================================
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"陣列元素如下 : {x} ")
print(f"x[2:]       = {x[2:]}")
print(f"x[:2]       = {x[:3]}")
print(f"x[0:3]      = {x[0:3]}")
print(f"x[1:4]      = {x[1:4]}")
print(f"x[0:9:2]    = {x[0:9:2]}")
print(f"x[-1]       = {x[-1]}")
print(f"x[::2]      = {x[::2]}")
print(f"x[2::3]     = {x[2::3]}")
print(f"x[:]        = {x[:]}")
print(f"x[::]       = {x[::]}")
print(f"x[-3:-7:-1] = {x[-3:-7:-1]}")
x2 = np.array(x, copy=True)
x3 = x2.copy()
print(x2)
print(x3)

#================================================
x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])
print(x)
print("x[:,:]   = 2-dim array")
print(x[:,:])

#================================================
x = np.arange(16)
print(x)
print(np.reshape(x,(2,8)))
print(np.reshape(x,(4,-1)))  # since 4 * 4 = 16
print(np.reshape(x, (-1,2))) # since 2 * 4 = 16

#================================================
x1 = np.arange(6).reshape(2,3)
print(f"array x1: \n{x1}")
x2 = np.arange(3,9).reshape(2,3)
print(f"array x2: \n{x2}")
x = np.hstack((x1,x2))
print(f"stack: \n{x}")

#================================================
# create image
fig = np.zeros((100, 200), dtype=np.uint8)
cv2.imshow("fig", fig)
cv2.waitKey(0)
cv2.destroyAllWindows()