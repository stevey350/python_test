
import numpy as np



data = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])

np.savetxt('sample.csv', data, delimiter=",")
