机器学习中，数据归一化是非常重要，如果不进行数据归一化，可能会导致模型坏掉或者训练出一个奇怪的模型。

# 为什么要进行数据归一化

现在有一个训练数据集，包含两个样本，内容如下：

|       | 肿瘤大小（cm） | 发现时间（day） |
| :---: | -------------- | --------------- |
| 样本1 | 1              | 200             |
| 样本2 | 5              | 100             |

以 k-近邻算法为例，“发现时间”的数值比“肿瘤大小”的数值大很多，样本间的距离被“发现时间”主导，训练出来的模型主要由“发现时间”影响，甚至“肿瘤大小”的影响可忽略不计。

解决方法就是将是数据映射到同一尺度，这就是数据归一化。

数据归一化的两个常用方式为：**最值归一化**和**均值方差归一化**。

# 最值归一化（normalization）

最值归一化就是将数据映射到 0～1 之间，适用于数据分布有明显边界的情况。将样本的特征值减去该特征的最小值，再除以该特征的取值区间，对应的数学公式为：
$$
x_{scale} = \frac{x-x_{min}}{x_{max}-x_{min}}
$$
使用 `np.random` 生成一个 50*2 的二维整形数组，并转换成浮点型：

```python
import numpy as np

X = np.random.randint(0, 100, size=(50, 2))
X = np.array(X, dtype=float)
```

对于第一列数据，$x_{min}$ = `np.min(X[:, 0])`，$x_{max}$ = `np.max(X[:, 0])`：

```python
X[:, 0] = (X[:, 0] - np.min(X[:, 0])) / (np.max(X[:, 0]) - np.min(X[:, 0]))
```

第二列数据同理：

```python
X[:, 1] = (X[:, 1] - np.min(X[:, 1])) / (np.max(X[:, 1]) - np.min(X[:, 1]))
```

此时样本的所有特征值都在 0～1 之间。

# 均值方差归一化（standardization）

​		均值方差归一化就是把所有数据归一到均值为0、方差为1的分布中。对于数据分布有无明显边界都适用。数学公式为：
$$
x_{scale} = \frac{x-x_{mean}}{s}
$$
$x_{mean}$：特征均值，$s$：特征方差。

同样使用 `np.random` 生成一个 50*2 的二维整形数组，并转换成浮点型：

```python
X2 = np.random.randint(0, 100, size=(50, 2))
X2 = np.array(X2, dtype=float)
```

对于第一列数据，$x_{mean}$ = `np.mean(X2[:, 0])`，$s$ = `np.std(X2[:, 0])`：

```python
X2[:, 0] = (X2[:, 0] - np.mean(X2[:, 0])) / np.std(X2[:, 0])
```

第二列数据同理：

```python
X2[:, 1] = (X2[:, 1] - np.mean(X2[:, 1])) / np.std(X2[:, 1])
```

可以查看 X2 各列的均值非常接近0，方差非常接近1：

```python
# np.mean(X2[:, 0])
-4.440892098500626e-18

# np.mean(X2[:, 1])
-1.2878587085651815e-16

# np.std(X2[:, 0])
0.9999999999999999

# np.std(X2[:, 1])
0.9999999999999999
```

# 对测试数据集进行归一化处理

前面都是在对训练数据集进行归一化处理，而对测试数据集的归一化处理有所不同。由于测试数据是在模拟真实环境，而在真实环境中很难拿到所有的测试数据的均值和方差，此时将测试数据集也进行上面的操作是错误的，正确的方法是利用训练数据集归一化的数据。

如测试数据集的最值归一化处理为：
$$
test_{scale} = \frac{test-min_{train}}{max_{train}-min_{train}}
$$
测试数据集的均值方差归一化处理为：
$$
test_{scale} = \frac{test-mean_{train}}{s_{train}}
$$
​	以均值方差归一化处理为例，Scikit Learn 中封装了 StandardScaler 类用于训练数据集和测试数据集的归一化处理。

以鸢尾花的数据为例：

```python
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

StandardScaler 类位于 preprocessing 模块中：

```python
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
```

将训练数据传入 `fit()` 方法中，该方法会保存训练数据的方差和均值，并返回 StandardScaler 实例本身：

```python
standardScaler.fit(X_train)
```

其中 `mean_`、`scale_` 属性保存了均值和方差：

```python
# standardScaler.mean_
array([5.83416667, 3.08666667, 3.70833333, 1.17      ])

# standardScaler.scale_
array([0.81019502, 0.44327067, 1.76401924, 0.75317107])
```

接着可以向 `transform()` 方法中传入训练数据和测试数据获取归一化处理后的数据：

```python
X_train = standardScaler.transform(X_train)
X_test = standardScaler.transform(X_test)
```

https://segmentfault.com/a/1190000016823628