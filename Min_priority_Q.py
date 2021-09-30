# Min Priority Queue inplement by min heap
# Usage:
# >>> PQ = [0]  # essential initialiazation, start index of ADT MUST be 1
# >>> Insert(PQ, node1)  # Insert node1 to PQ. node1 must be Node().
# >>> ExtractMax(PQ)  # heap.ExtractMax() action.
#
# !!!!  Reference: Data Structures and Analysis - Lecture Notes for CSC263 (Version 0.2) - David Liu

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __repr__(self):
        return f"Node({self.value}, p={self.priority})"

PQ = [0]  # index of PQ starts from 1. PQ is empty iff PQ == [0]

def FindMax(PQ):
    if PQ == [0]:
        return
    return PQ[1]


def ExtractMax(PQ):
    if PQ == [0]:
        return

    temp = PQ[1]
    PQ[1] = PQ[len(PQ) - 1] # Replace the root with the last leaf
    PQ.pop()
    # Bubble down
    i = 1
    while i * 2 <= len(PQ) - 1:
        curr_p = PQ[i].priority
        left_p = PQ[2*i].priority
        right_p = PQ[2*i + 1].priority if 2*i + 1 < len(PQ) else float("-inf")# -inf if not exist
        # heap property is satisfied
        if curr_p <= left_p and curr_p <= right_p:
            break
        # left child has higher priority
        elif left_p <= right_p:
            PQ[i], PQ[2*i] = PQ[2*i], PQ[i]
            i = 2*i
        # right child has higher priority
        else:
            if 2*i + 1 < len(PQ):
                PQ[i], PQ[2*i + 1] = PQ[2*i + 1], PQ[i]
            i = 2*i + 1
    return temp

def Insert(PQ, x: Node):
    # PQ.size = PQ.size + 1
    # PQ[PQ.size].item = x
    PQ.append(x)  # x should be type(Node)
    # PQ[PQ.size].priority = priority 
    i = len(PQ) - 1
    while i > 1:
        curr_p = PQ[i].priority
        parent_p = PQ[i // 2].priority    
        if curr_p >= parent_p: # heap property satisfied, break
            break
        else:
            PQ[i], PQ[i // 2] = PQ[i // 2], PQ[i]
            i = i // 2

def DecreasePriority(PQ, i, p):
    """ p < PQ[i].p. make sure that is decreasing, not increasing"""
    if PQ[i].priority < p:
        print("something wrong in DecreasePriority")
        return 

    PQ[i].priority = p
    Bubbleup(PQ, i)

def Bubbleup(PQ, i):
    curr = i
    while i // 2 >= 1:
        curr_p = PQ[curr].priority
        parent_p = PQ[curr // 2].priority if not PQ[curr // 2] == 0 else float("-inf")

        if parent_p < curr_p:
            break
        else:
            PQ[curr], PQ[curr // 2] = PQ[curr // 2], PQ[curr]
        curr //= 2


   


if __name__ == "__main__":
    node1 = Node("a", 1)
    node2 = Node("c", 3)
    node3 = Node("b", 7)
    node4 = Node("e", 5)
    node5 = Node("f", 4)
    node6 = Node("g", 9)
    node7 = Node("h", 8)
    node8 = Node("i", 100)

    Insert(PQ, node1)
    Insert(PQ, node5)
    Insert(PQ, node3)
    Insert(PQ, node2)
    Insert(PQ, node7)
    Insert(PQ, node4)
    Insert(PQ, node6)
    Insert(PQ, node8)

    print(PQ)
    DecreasePriority(PQ, 8, 0)
    print(PQ)
    