import numpy as np

arr = np.array(12)
arr1 = np.array([12,13])
arr2 = np.array([[1,2],[3,4]])
arr3 = np.array([[1,2],[2,3],[45,22]])
arr4 = np.array([[[1,2],[3,4]],[[11,12],[22,33]],[[55,66],[20,30]]])

print(arr)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)