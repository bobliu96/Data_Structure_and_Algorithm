class Graph:
    def __init__(self, size):
        self.graph = []
        self.size = size

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        stack.append(v)

    def topologicalSort(self):
        visited = [False] * self.size
        stack = []

        for i in range(self.size):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        return stack[: : -1]


graph = Graph(6)
graph.addEdge(5,2)
graph.addEdge(5,0)
graph.addEdge(4,0)
graph.addEdge(4,1)
graph.addEdge(2,3)
graph.addEdge(3,1)
print(Graph.topologicalSort())
