from Graph import *

def MST(g: Graph) -> int:
    """ flaw: not able to combine two sets."""
    result = Graph(len(g))
    used = []  # indicate the vertices that already met
    entire = sorted(g.edges, key=lambda x: x.weight)
    for each in entire:
        if each.edge[0] in used and each.edge[1] in used:
            pass
        else:
            if each.edge[0] not in used:
                used.append(each.edge[0])
            if each.edge[1] not in used:
                used.append(each.edge[1])
            result.add_edge(each.edge)
            

    return result 


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

    print(MST(g))