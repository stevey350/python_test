
'''
列表基本操作: 更新、追加、删除、拼接、截取
'''
def list_basic():
    list = ['Google', 'Runoob', 1997, 2000]
    
    # 更新
    list[2] = 2001
    print ("After update: ", list)
    
    # 追加
    list.append('Baidu')        # Note: append是直接将元素添加到list中，返回值是None
    print ("After append ", list)

    # 删除
    del list[2]
    print("After del: ", list)

    # 拼接
    list2 = ['Google', 'Runoob', 'Taobao']
    list3 = list + list2
    print(list3)

    # 截取
    print(list3[-2])        # 最右侧为-1，右侧倒数第二个为-2

'''
Python列表list包含如下方法: append, count, extend, index, insert, pop, remove, reverse, sort, clear, copy
'''
def list_func():
    pass


'''
Python 中的 [:-1] 和 [::-1]

b = a[i:j]        # 假设a是一个1维列表

# i表示起始下标, 当i缺省时, 默认为0, 即a[:3]相当于a[0:3]
# j表示终止下标(不包括), 当j缺省时, 默认为len(alist), 即a[1:]相当于a[1:10]
# 当i,j都缺省时, a[:]就相当于完整复制一份a

b = a[i:j:s]    
# i, j与上面一枯
# s表示步进, 缺省为1, 所以a[i:j:1]相当于a[i:j]
# 当s<0时, i缺省时, 默认为-1. j缺省时, 默认为-len(a)-1
# 所以a[::-1]相当于a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。
'''
def list_index():
    a = 'python'
    b = a[::-1]
    print(b) #nohtyp
    c = a[::-2]
    print(c) #nhy
    #从后往前数的话，最后一个位置为-1
    d = a[:-1]  #从位置0到位置-1之前的数
    print(d)  #pytho
    e = a[:-2]  #从位置0到位置-2之前的数
    print(e)  #pyth


if __name__ == "__main__":
    list_basic()
