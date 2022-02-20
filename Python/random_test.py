import numpy as np
import random
from matplotlib import pyplot as plt 

# 在0-2*pi的区间上生成100个点作为输入数据
X = np.linspace(0, 2*np.pi, 100, endpoint=True)
Y = np.sin(X)

# 对输入数据加入gauss噪声
# 定义gauss噪声的均值和方差
mu = 0
sigma = 0.12
for i in range(X.size):
    X[i] += random.gauss(mu, sigma)
    Y[i] += random.gauss(mu, sigma)

# 画出这些点
plt.plot(X,Y,linestyle='',marker='.')
plt.show()

