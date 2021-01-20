import os
from tkinter import *
from tkinter import filedialog

DESKTOP = "C:\\Users\\Administrator\\Desktop"

root = Tk()
root.title("dir dialog")
root.filename = filedialog.askdirectory(initialdir=os.environ["HOMEPATH"]+"\\Desktop", title='select a file.')
print(root.filename, type(root.filename))

root.mainloop()