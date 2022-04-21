
import numpy as np

data = np.asarray([ [1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9],
                    [1, 5, 2]])

index = np.where(data[:, 1] == 5)
print("index: ", index)
data1 = np.delete(data, index, axis=0)  # axis = 0按行删除，axis=1按列删除
print("data1: \n", data1)