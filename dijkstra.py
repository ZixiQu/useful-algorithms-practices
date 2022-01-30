from Min_priority_Q import *

def dijkstra(V, E, start):
    """ 
    V = [0, 1 ,2]  # town 0, 1 and 2
    E = [[0, 1, 15], [1, 2, 30]]
    start = 0
    dest = 2

    return a tuple(d, p) where:
    d is the shortest length from start point to each points
    p is the privious node of each node at finishing time 
    """
    q = [0]  # min PQ initialization
    X = []
    d = {}
    p = {}
    for v in V:
        if v != start:
            Insert(q, Node(v, float("inf")))
            d[v] = float("inf")
    Insert(q, Node(start, 0))
    d[start] = 0

    while len(X) != len(V):
        curr_v = ExtractMin(q)
        if curr_v == None:
            break
        # print(curr_v.priority)
        curr_v = curr_v.value

        X.append(curr_v)
        for edge in E:
            if edge[0] == curr_v:
                u, weight = edge[1], edge[2]
                if d[u] > d[curr_v] + weight:
                    d[u] = d[curr_v] + weight
                    p[u] = curr_v
                    for i in range(1, len(q)):
                        if q[i].value == u and d[u] < q[i].priority:
                            DecreasePriority(q, i, d[curr_v] + weight)
                            break
    return d, p


if __name__ == '__main__':

    V = ["A", "B", "C", "D", "E"]  # town 0, 1 and 2
    E = [["A", "D", 1], ["D", "B", 2], ["A", "B", 6], ["D", "E", 1], ["B", "E", 2], ["E", "B", 2], ["B", "C", 5], ["E", "C", 5]]
    start = "A"

    print(dijkstra(V, E, start))