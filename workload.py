# An light-weight script that stores the missions recently
# Actions: display(): display all current missions by priority
#          increasePriority(): as name
#          crossout(mission: default=top)
#          add(mission, priority=1 of {"high", "recently", "low"}): add mission to mission list

# run script...
# >>> current missions: 
# ... ....
# >>> display()
# ... *missions ...
# >>> add("assignment 2 @ 10.30 9p.m", -5)
# >>> display()
# ... missions list with new mission ...
# >>> 


from HeapPractice import *

FILE = "heap.txt"

class WorkLoad(PriorityQueue):
    def __init__(self, values):
        super().__init__(values)

    def display(self):
        for each in self._values:
            print(each.value)
            print()


if __name__ == "__main__":
    node1 = Node("csc369 a1 Oct 6 @ 10 pm", 10)
    node2 = Node("csc373 ps1 Oct 1, 22:00", 5)
    node3 = Node("csc347 A1 Due Oct 8th, 2021 (11:55pm Toronto time)", 1)

    missions = []
    weight = 0

    with open(FILE) as f:
        for each in f:
            if each.strip() != "":
                node = Node(each.strip(), weight)
                weight -= 1


    wl = WorkLoad([node1, node2, node3])
    wl.display()
