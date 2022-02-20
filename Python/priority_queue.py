
from queue import PriorityQueue     #优先级队列

'''------------------------------优先级队列-----------------------------'''
q = PriorityQueue()

# 格式：q.put((数字,值))
#特点：数字越小，优先级越高
q.put((1, 'ssj'))
q.put((1, 'lori'))
q.put((-1, 'Jseon'))
q.put((10, 'King'))

print('q is empty? ', q.empty())

while not q.empty():
    print(q.get())
