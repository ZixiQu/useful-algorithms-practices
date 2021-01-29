from typing import List, Any, Union

class Node:
    def __init__(self, value: Any, weight: Union[float, int]=0) -> None:
        self.value = value
        self.weight = weight

    def __str__(self) -> str:
        return f"{self.value}: {self.weight}" 

    def __repr__(self) -> str:
        return self. __str__()


class PriorityQueue:
    """ 
    The Priority Queue based on int. 
    """
    def __init__(self, values: List[Node]=[]) -> None:
        """ Init PQ"""
        self._values = []
        for each in values:
            self.insert(each)
    
    def __repr__(self) -> str:
        """ the repr interface. """
        return str(self._values)

    def __str__(self) -> str:
        return str(self._values)

    def insert(self, value: Node) -> None:
        """ insert <value> in PQ"""
        self._values.insert(0, value)
        index = 1
        child1 = None
        child2 = None 
        while 1:
            curr_index = index - 1
            left_child_index = index * 2 - 1
            right_child_index = index * 2
            if left_child_index < len(self._values):
                child1 = self._values[left_child_index]
            if right_child_index < len(self._values):
                child2 = self._values[right_child_index]

            if not child1 and not child2:
                return
            if not child1:
                child1 = Node(None, float("-inf"))
            if not child2:
                child2 = Node(None, float("-inf"))

            

            if self._values[curr_index].weight > child1.weight and self._values[curr_index].weight > child2.weight:
                return

            elif child1.weight > child2.weight:
                self._values[curr_index], self._values[left_child_index] = self._values[left_child_index], self._values[curr_index]
            else:
                self._values[curr_index], self._values[right_child_index] = self._values[right_child_index], self._values[curr_index]
            index *= 2
            child1 = None
            child2 = None 
    

    def extractMax(self) -> Any:
        """ "dequeue" the Max """
        if len(self._values) == 0:
            return 
        result = self._values.pop(0)
        if len(self._values):
            bottom = self._values.pop()
            self.insert(bottom)
        return result

    def max(self) -> Any:
        """ peak the max"""
        return self._values[0]

    def increasePriotity(self, value) -> bool:
        """ if <value> in PQ, """
        pass

def heapSort(lst: List[int]) -> List:
    """ sort <lst> using heap sort algorithm"""
    result = []
    PQ = PriorityQueue([Node(None, i) for i in lst])
    for _ in range(len(PQ._values)):
        result.append(PQ.extractMax().weight)
    return result[::-1]


if __name__ == "__main__":
    
    node1 = Node("Kanye", 10.0)
    node2 = Node("xdd", 9.9)
    node3 = Node("someone", 5)

    target = [Node(None, i) for i in range(10)]
    import random
    random.shuffle(target)
    PQ = PriorityQueue(target)
    print(PQ)
    
    for _ in range(10):
        print(PQ.extractMax())

    target = [5,3,1,54,6,7,1,2,4]
    print(heapSort(target))

    # print(PQ)

    