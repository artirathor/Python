import numpy as np
arr = np.array([1,2,3,4])
arr_new = arr.copy()
arr[2] = 100
print(arr)
print(arr_new)

import numpy as np
arr1 = np.array([["a","b"],["c","d"]])
newarr1 = arr1.copy()
arr1[1,1] = "2"
print(newarr1)
print(arr1)
