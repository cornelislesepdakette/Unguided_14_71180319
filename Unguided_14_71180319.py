class Graph:
    def __init__(self):
        self._data = {}
    def addVertex(self, key):
        if key not in self._data:
            self._data[key] = set()
    def vertex(self):
        print("\nSeluruh Node = ",end= "")
        for key, value in self._data.items():
            print(key, end=" ")
        print()
    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x)
    def edge(self):
        print("Seluruh Edge = ", end="")
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
        for item in listEdge:
            print(item, end=" ")
    # def findPath(self, x, y):
    #     visited = []
    #     self.bfs(x, y, visited)
    def bfs(self, node):
        visited = set()
        visited.add(node)
        queue = set()
        queue.add(node)
        print("\nTraversing BFS = ",end="")
        while queue:
            s = queue.pop()
            print(s, end=" ")
            for neighbour in self._data:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.add(neighbour)

graph = Graph()
graph.addVertex("a")
graph.addVertex("b")
graph.addVertex("c")
graph.addVertex("d")
graph.addVertex("e")
graph.addVertex("f")
graph.addVertex("g")

graph.addEdge("a","b")
graph.addEdge("b","c")
graph.addEdge("b","d")
graph.addEdge("c","e")
graph.addEdge("c","g")
graph.addEdge("d","e")
graph.addEdge("e","f")

graph.vertex()
graph.edge()
graph.bfs("a")