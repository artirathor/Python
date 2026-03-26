import numpy as np
arr = np.array([1,3,5,8,9])
new_arr = arr.copy()
arr[1] = 10
print(new_arr)
print(arr)