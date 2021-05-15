from helperclass import *

class Graph:
    def __init__(self):
        """ implementing graph using adjacency list"""
        self.vertices = []
        self.edges = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.edges[vertex] = LList()

    def add_edge(self, f, to):
        """ <f> stands for from"""
        assert f in self.vertices

        self.edges[f].append(Node(to))

    def check_valid(self):
        """ Graph is valid (valid: perform operations without error arise) iff:
        1. no repeat vertices
        2. no invalid edges (e.g: vertices: [1,2,3], edges: {3: 4 -> None})
        """
        hashtable = {}
        for each in self.vertices:
            if each in hashtable:
                raise VertexRepeatError("1. {} repeat.".format(each))
            hashtable[each] = 0

        for each in self.edges:
            curr = self.edges[each].head
            while curr:
                if curr.value not in self.vertices:
                    raise ValueError("2 {} not exists".format(curr.value))
                curr = curr.next

    class VertexRepeatError(Exception):
        pass

    def BFS(self, start, target):
        self.check_valid()
        if start not in self.vertices or target not in self.vertices:
            raise ValueError("BFS: vertex not found")
        color_table = {}
        for each in self.vertices:
            color_table[each] = "white"
        q = Queue()
        q.enqueue(start)
        while not q.is_empty():
            curr = q.dequeue()
            if curr == target:
                return True

            llcurr = self.edges[curr].head
            while llcurr is not None:
                if color_table[llcurr.value] == "white":
                    color_table[llcurr.value] = "grey"
                    q.enqueue(llcurr.value)
                llcurr = llcurr.next

            color_table[curr] = "black"
        return False




if __name__ == "__main__":
    g = Graph()
    for i in range(1, 9):
        g.add_vertex(i)
    g.add_edge(2, 5)
    g.add_edge(3, 2)
    g.add_edge(3, 4)
    g.add_edge(4, 3)
    g.add_edge(5, 7)
    g.add_edge(8, 1)
    g.add_edge(8, 6)
    print(g.BFS(6, 7))




