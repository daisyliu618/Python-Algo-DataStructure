graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, start):
    queue = [start]
    seen = set()
    seen.add(start)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)


BFS(graph, "A")
print("========")


# Deques have O(1) speed for appendleft() and popleft()
# while lists have O(n) performance for insert(0, value) and pop(0).

from collections import deque
def bfs(graph, node):
    visited = []
    q = deque([node])
    while deque:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            q += graph[n] - set(visited)
    return visited


# 给每个node加上parent 把图变成树状结构

def BFS1(graph, start):
    queue = [start]
    seen = set()
    seen.add(start)
    parent = {start: None}
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        # print(vertex)
    return parent


# 把图变成树状结构
parent = BFS1(graph, "E")


# for key in parent:
#     print(key, parent[key])


# 通过BFS从终点寻找起始点

# v = "B"
# while v is not None:
#     print(v)
#     v = parent[v]
# print("========")


def DFS(graph, start):
    stack = [start]
    seen = set()
    seen.add(start)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)


# DFS(graph, "A")

def dfs(graph, node):
    visited = []
    stack = [node]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited


import heapq
import math

# 如何使用priorityQueue
# pqueue = []
# heapq.heappush(pqueue, (1, "A"))
# heapq.heappush(pqueue, (7, "B"))
# heapq.heappush(pqueue, (3, "C"))
# heapq.heappush(pqueue, (6, "D"))
# heapq.heappush(pqueue, (2, "E"))
#
# print(pqueue)

graph1 = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6},
}


# print(graph1["A"])
# print(graph1["A"])
# print(graph1["A"].keys())
# print(graph1["C"]["B"])

def init_distance(graph, start):
    distance = {start: 0}
    for vertex in graph:
        if vertex != start:
            distance[vertex] = math.inf
    return distance


def dijkstra(graph, start):
    pqueue = []
    heapq.heappush(pqueue, (0, start))
    seen = set()
    parent = {start: None}
    distance = init_distance(graph, start)
    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph1[vertex][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph1[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph1[vertex][w]
        # print(vertex)
    return parent, distance


parent, distance = dijkstra(graph1, "A")
print(parent)
print(distance)

# https://www.youtube.com/watch?v=bD8RT0ub--0
