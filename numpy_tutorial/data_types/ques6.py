import numpy as np
arr = np.array([1,2,3,4])
print(arr.dtype)

import numpy as np
arr1 = np.array([5,6,7,8], dtype = "i4")
print(arr1)
print(arr1.dtype)

import numpy as np
arr2 = np.array(["apple","banana","grapes","coconut"])
print(arr2.dtype)
print(arr2[2])
print(arr2[0:3])

import numpy as np
arr3 = np.array([1,2,3,4],dtype = "f")
print(arr3.dtype)
print(arr3)

import numpy as np

arr4 = np.array([1.1, 2.1, 3.1])
newarr = arr4.astype('i')
print(arr4)
print(newarr)
print(newarr.dtype)

import numpy as np
arr5 = np.array(["a","b","c"])
new_arr5 =arr5.astype(bool)
print(new_arr5.dtype)


