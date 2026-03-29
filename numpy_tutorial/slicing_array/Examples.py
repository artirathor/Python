import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(arr[1])
print(arr.ndim)
print(arr.shape)
print(arr[0:2])
print(arr[ :3])
print(arr[2:])

import numpy as np
arr1 = np.array([[1,2,3,4],[5,6,7,0]])
print(arr1)
print(arr1.shape)
print(arr1.ndim)
print(arr1[1,3])
print(arr1[0:2,2])
print(arr1[1,1:3])
print(arr1[0:1,0:3])

import numpy as np
arr2 = np.array([[[1,2,3],[4,5,6]],[[5,6,7],[8,9,10]]])
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2[0,1,1])
print(arr2[1,0,0])
print(arr2[1,0:2,2])