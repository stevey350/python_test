
from typing import List, Dict, Tuple, NewType

# 使用了类型提示 https://www.cnblogs.com/poloyy/p/15145380.html
# 
num: int = 0                # int 变量，默认值为 0
bool_var: bool = True       # bool 变量，默认值为 True
dict_var: Dict = {}         # 字典变量，默认为空
primes: List[int] = []      # 列表变量，且列表元素为 int
t: Tuple[int, ...] = None   # 元组打包

num = "123"             # 它并不会报错，但是会有warning，是IDE的智能语法提示
bool_var = 123
dict_var = []
primes = ["1", "2"]
t = (1, 2, 3)

print(num, bool_var, dict_var, primes, t)


# 类型别名 https://www.cnblogs.com/poloyy/p/15153883.html
# 
# 1. 变量例子
vector = List[float]        # 别名
var: vector = [1.1, 2.2]    # 等价写法
var: List[float] = [1.1, 2.2]

# 2.函数例子
vector_list_es = List[float]                    # float 组成的列表别名
vector_dict = Dict[str, vector_list_es]         # 字典别名
vector_list = List[vector_dict]                 # 字典组成列表别名

vector = List[Dict[str, List[float]]]           # vector_list 等价写法，不用别名的话，有点像套娃

# 函数， 其中->常常出现在python函数定义的函数名后面，为函数添加元数据,描述函数的返回类型
def scale(scalar: float, vector: vector_list) -> vector_list:
    for item in vector:
        for key, value in item.items():
            item[key] = [scalar * num for num in value]
    print(vector)
    return vector


scale(2.2, [{"a": [1, 2, 3]}, {"b": [4, 5, 6]}])

# NewType 自定义创一个新类型
# 主要用于类型检查
# NewType(name, tp) 返回一个函数，这个函数返回其原本的值
# 静态类型检查器会将新类型看作是原始类型的一个子类
# tp 就是原始类型
UserId = NewType('UserId', int)
def name_by_id(user_id: UserId) -> str:
    print(user_id)

UserId('user')          # Fails type check
num = UserId(5)         # type: int

name_by_id(42)          # Fails type check
name_by_id(UserId(42))  # OK

print(type(UserId(5)))  # 可以看到 UserId 其实也是 int 类型


# TypeVar
T = TypeVar('T')        # 可以任意类型

def test(name: T) -> T:
    print(name)
    return name

test(11)
test("aa")

AA = TypeVar('AA', int, str)    # 可以是int，也可以是str类型
 
num1: AA = 1
num2: AA = "123"
print(num1, num2)
 
num3: AA = []               # 提示: expected type 'AA', got 'list' instead

