import numpy as np
arr = np.array([1,2,3,4])
print(arr)
print(arr.ndim)
print(arr[0])

import numpy as np
arr1 = np.array([[2,3,4,5,6]])
print(arr1)
print(arr1.ndim)
print(arr1[0,2])

import numpy as np
arr2 = np.array([[[1,2]],[[3,4]],[[4,5]]])
print(arr2)
print(arr2.ndim)
print(arr2[1,0,1])

import numpy as np
arr3 = np.array([[[[1,2],[3,4]],[[5,6],[7,8]],[[9,0],[111,121]]],[[[11,12],[31,41]],[[15,16],[17,18]],[[19,10],[11,12]]]])
print(arr3)
print(arr3.shape)
print(arr3.ndim)
print(arr3[1,2,1,1])