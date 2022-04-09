
from operator import index
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

def pd_series_test():
    """
    Series是⼀种类似于⼀维数组的对象，由一组数据和对应的一组标签组成
    """
    # obj = pd.Series([4, 7, -5, 3])
    # obj = Series([4, 7, -5, 3])
    obj = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])  # 创建时指定索引
    print(type(obj))
    print("obj values: \n", obj.values)         # 数据属性
    print("obj index: \n", obj.index)           # 标签索引属性
    print("obj['a']: ", obj['a'])               # 与Numpy相比，可通过索引取值
    print("obj[...]: \n", obj[['d', 'b', 'a']]) 
    print(obj[obj > 0])         # 布尔型数组进⾏过滤
    print(obj * 2)              # 标量乘法
    print(np.exp(obj))          # 应用数学函数

    # 将Series看作是一个定长的有序字典
    dict = {'Ohio': 35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
    dict_index = ['California', 'Ohio', 'Oregon','Utah']
    obj2 = pd.Series(dict, index=dict_index)
    print(pd.isnull(obj2))      # pandas判断数据是否缺失
    print(obj2.isnull())        # Serial也有类似的方法


def pd_dataframe_test():
    # 第一种数据形式
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    # frame = pd.DataFrame(data)
    frame = pd.DataFrame(data, columns=['year', 'state', 'pop'],    # 指定列顺序
                               index=['one', 'two', 'three', 'four', 'five', 'six'])    
    print(frame)
    # 行的获取
    frame_col = frame['year']         # 将DataFrame的列获取为⼀个Series
    print(type(frame_col))
    
    # 列的获取
    frame_row = frame.loc['three']      # loc是属性
    print(frame_row)

    # 某个单元格
    print(frame.iloc[0, frame.columns.get_loc('state')])

    # 创建新的列
    frame['eastern'] = frame['state'] == 'Ohio'
    print(frame)

    # 删除某一列
    del frame['eastern']
    print(frame)

    # 第二种数据形式：嵌套字典
    nested_dict = {'Nevada': {2001: 2.4, 2002: 2.9},
                   'Ohio':   {2000: 1.5, 2001: 1.7,	2002: 3.6}}
    frame2 = pd.DataFrame(nested_dict)  # 外层key为列索引，内层key为行索引
    print(frame2)
    print(frame2.T)     # 行列转置


if __name__ == "__main__":
    print("Hello, pandas")
    # pd_series_test()
    pd_dataframe_test()
