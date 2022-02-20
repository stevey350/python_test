# 非常好的博客
# https://www.redblobgames.com/pathfinding/a-star/introduction.html
#

#
# Breadth First Search
# 
'''
frontier = Queue()
frontier.put(start)
came_from = dict()      # 字典dict()存放一系列key-value键值对
came_from[start] = None

# 向外搜索扩展
while not frontier.empty():
    current = frontier.get()

    if current == goal:
        break;

    for next in graph.neighbors(current):   # 这里的graph有待细化
        if next not in came_from:
            frontier.put(next)
            came_from[next] = current       # key为某个节点，value为上一个节点

# 逆向遍历came_from，以生成路径
current = goal 
path = []
while current != start: 
    path.append(current)
    current = came_from[current]
path.append(start) # optional
path.reverse() # optional

'''

#
# Dijkstra's Algorithm
#
'''
frontier = PriorityQueue()
came_from = dict()
cost_so_far = dict()        # 某个点到起始节点start的距离(损失)

frontier.put(start, 0)
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
   current = frontier.get()     # 优先取出数字小的值（数字越小，优先级越高）

   if current == goal:
      break
   
   for next in graph.neighbors(current):
      new_cost = cost_so_far[current] +         # 当前节点到起始节点start的损失
                 graph.cost(current, next)      # 当前节点与下个节点next的损失
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost
         frontier.put(next, priority)
         came_from[next] = current
'''

from queue import PriorityQueue

class Graph:
    def __init__(self, num):
        self.all_nodes = []
        for x in range(20):
            for y in range(10):
                self.all_nodes.append((x, y))
    
    def neighbors(self, node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            neighbor = (node[0]+dir[0], node[1]+dir[1])
            if neighbor in self.all_nodes:
                result.append(neighbor)
        return result

    # weighted graph需要提供cost方法
    def cost(self, current, next):
        return 1

    def heuristic(self, goal, next):
        # Manhattan distance
        return abs(next[0] - goal[0]) + abs(next[1] - goal[1])


if __name__ == '__main__':

    print("Hello, A star algorithm")
    frontier = PriorityQueue()
    came_from = dict()
    cost_so_far = dict()
    graph = Graph(10)

    start = (0, 0)              # 起始节点
    goal = (15, 8)              # 目标节点
    frontier.put(start, 0)
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            print("Reach goal taget")
            break
        for next in graph.neighbors(current):
            # new_cost = cost_so_far[current] + graph.cost(current, next)
            new_cost = cost_so_far[current] + 1     # 栅格图，相邻边的权重简化为1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + graph.heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    # 逆向遍历came_from，以生成路径
    current = goal 
    path = []
    while current != start: 
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()      # optional
    print("path: ")
    print(path)
