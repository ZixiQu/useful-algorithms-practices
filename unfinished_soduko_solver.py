import tkinter as Tkinter

GRID = [[0, 0, 0, 2, 6, 0, 7, 0, 1], 
        [6, 8, 0, 0, 7, 0, 0, 9, 0], 
        [1, 9, 0, 0, 0, 4, 5, 0, 0], 
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0], 
        [0, 5, 0, 0, 0, 3, 0, 2, 8], 
        [0, 0, 9, 3, 0, 0, 0, 7, 4], 
        [0, 4, 0, 0, 5, 0, 0, 3, 6], 
        [7, 0, 3, 0, 1, 8, 0, 0, 0]]

root = Tkinter.Tk()
root.geometry("300x300")


def render():
    global GRID
    global root 
    for r in range(9):
       for c in range(9):
          Tkinter.Label(root, text= GRID[r][c], borderwidth=3).grid(row=r,column=c)
    root.mainloop()

def foo(num):
    return (num//3)*3

def possible(x, y, num):
    global GRID
    for i in range(9):
        if GRID[x][i] == num:
            return False
    for j in range(9):
        if GRID[j][y] == num:
            return False
    for i in range(foo(x), foo(x) + 3):
        for j in range(foo(y), foo(y) + 3):
            if GRID[i][j] == num:
                return False
    return True 

def completed():
    global GRID
    for i in range(9):
        for j in range(9):
            if GRID[i][j] == 0:
                return False
    return True

def solve():
    if completed():
        return 
    else:
        global GRID
        unsolved = []
        for i in range(9):
            for j in range(9):
                if GRID[i][j] == 0:
                    unsolved.append((i, j))
        for each in unsolved:
            x, y = each[0], each[1]
            for guess in range(1, 10):
                if possible(x, y, guess):
                    GRID[x][y] = guess

def solve_ans():
    global GRID
    for x in range(9):
        for y in range(9):
            if GRID[x][y] == 0:
                for n in range(1,10):
                    if possible(x, y, n):
                        GRID[x][y] = n
                        solve()
                        GRID[x][y] = 0
                return 



if __name__ == "__main__":
    for i in range(1, 10):
        print(possible(0, 2, i), i)
        


    # solve_ans()
    # render()
    
    