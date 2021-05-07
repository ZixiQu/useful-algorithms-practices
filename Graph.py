from __future__ import annotations
from typing import Union
import random

class Edge:
    def __init__(self, edge: tuple[int, int], weight: int=0):
        self.edge = edge
        self.weight = weight

    def __eq__(self, other: Union[tuple, Edge]):
        if not isinstance(other, tuple) and not isinstance(other, Edge):
            raise TypeError(f"{other} is not type tuple or Edge: {type(other)}")
        if isinstance(other, tuple):
            return self.edge == other or self.edge == (other[1], other[0])
        if isinstance(other, Edge):
            return self.edge == other.edge or self.edge == (other.edge[1], other.edge[0])
        

    def __repr__(self):
        return "{}{}".format(self.edge, f": {self.weight}" if self.weight != 0 else "")

    def change_weight(self, value):
        self.weight = value

class Graph:
    def __init__(self, v_num: int=5, full: bool=False):
        self.vertices = [i for i in range(v_num)] 
        self.edges = []
        if full:
            for i in range(len(self.vertices)):
                for j in range(i):
                    self.edges.append(Edge((i, j)))

    def __str__(self):
        return f"{self.edges}"

    def __len__(self) -> int:
        """ return number of vertices"""
        return len(self.vertices)

    def change_weight(self, edge, value) -> bool:
        if not isinstance(edge, tuple) or len(edge) != 2:
            raise TypeError(f"edge invalid: {edge}")
        for each in self.edges:
            if each == edge:
                each.change_weight(value)
                return True
        return False

    def add_edge(self, edge: tuple) -> bool:
        for each in self.edges:
            if each == edge:
                return False
        self.edges.append(Edge(edge))
        return True


if __name__ == "__main__":
    g = Graph(5)
    print(g.add_edge((0, 1)))
    print(g.change_weight((0, 1), 8))

    print(g.add_edge((0, 4)))
    print(g.change_weight((0, 4), 10))

    print(g.add_edge((1, 2)))
    print(g.change_weight((1, 2), 2))

    print(g.add_edge((1, 3)))
    print(g.change_weight((1, 3), 3))

    print(g.add_edge((2, 3)))
    print(g.change_weight((2, 3), 12))

    print(g.add_edge((1, 4)))
    print(g.change_weight((1, 4), 5))

    print(g.add_edge((3, 4)))
    print(g.change_weight((3, 4), 5))


    print(g)