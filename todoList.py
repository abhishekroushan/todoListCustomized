"""
Author: Abhishek Roushan (abhishek.roushan12@gmail.com)
Open source code for a cutom todo list solution
The user will be able to add fields, add attributes and 
sort them using different attributes
Language: Python
"""
from tkinter import *

class Attributes(object):
    def __init__(self, d):
        self.d = d
    def reset(self):
        self.d = {}
    def valueForKey(self, key:str):
        if key not in self.d:
            print("key not found: ", key)
            return None
        return self.d[key]
    def addKeyValue(self, key, value):
        self.d[key]=value
    def serialize(self):
        result = "{"
        for k,v in self.d.items():
            result+=k+":"+str(v)+","
        result+="}"
        return result

class TodoListItem(object):
    def __init__(self, item:str, attributes=Attributes({})):
        self.item = item
        self.attributes = attributes
    def getItem(self):
        return self.item
    def getAttributes(self):
        return self.attributes
    def getAttributesSerialized(self):
        return self.attributes.serialize()
    def reset(self):
        self.item = None
    def setAttributes(self, attributes):
        # attributes = Attributes
        self.attributes = attributes
    def addAttribute(self, key, value):
        self.attributes.addKeyValue(key, value)
    def valueForAttributeKey(self, key):
        return self.attributes.valueForKey(key)

class TodoList(object):
    def __init__(self):
        self.list = []
    def addTodoListItem(self, todoListItem):
        self.list.append(todoListItem)
    def print(self):
        print("Todo List:")
        for i,l in enumerate(self.list):
            print(i,":", l.getItem(), "--", l.getAttributesSerialized())
    def sortByAttributeKey(self, key:str):
        self.list.sort(key=lambda x: x.valueForAttributeKey(key))

def createTodoListDummy():
    tl = TodoList()
    tl.addTodoListItem(TodoListItem("buy groceries", 
                       Attributes({"priority":1, "time required":2, "impact":8.5})))
    tl.addTodoListItem(TodoListItem("workout",
                       Attributes({"priority":2, "time required":3.5, "impact":4.5})))
    tl.addTodoListItem(TodoListItem("finish L1 cache implementation",
                       Attributes({"priority":3, "time required":1.5, "impact":1.5})))
    tl.addTodoListItem(TodoListItem("study Freakonomics",
                       Attributes({"priority":4, "time required":1, "impact":1})))
    print("unsorted todo list")
    tl.print()
    sortByAttributeKey = "time required"
    print("sort todo list by time required")
    tl.sortByAttributeKey(sortByAttributeKey)
    tl.print()

class MyTodoListWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text = "Todo item")
        self.lbl1.grid(row=10, column= 0)
        self.lbl2 = Label(window, text = "Priority")
        self.lbl2.grid(row=10, column= 1)
        self.lbl3 = Label(window, text = "Time required")
        self.lbl3.grid(row=10, column= 2)
        self.lbl4 = Label(window, text = "Impact")
        self.lbl4.grid(row=10, column= 3)
        self.rowOffset = 20
        self.rows = []
        self.initGrid(window, 5,4)
    def initGrid(self, window, numRows:int, numCols:int):
        for i in range(numRows):
            cols = []
            for j in range(numCols):
                e = Entry(window, relief=GROOVE)
                e.grid(row=i+self.rowOffset, column=j, sticky=NSEW)
                e.insert(END, '%d.%d' % (i, j))
                cols.append(e)
            self.rows.append(cols)

    def showTodoList(self):
        pass


def createUIForToDoList():
    window=Tk()
    # btn=Button(window, text="This is Button widget", fg='blue')
    # btn.place(x=80, y=100)
    # lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
    # lbl.place(x=60, y=50) 
    myWin = MyTodoListWindow(window)
    # lbl1 = Label(window, text = "Todo item")
    # lbl1.grid(row=10, column= 0)
    # lbl2 = Label(window, text = "Priority")
    # lbl2.grid(row=10, column= 1)
    # lbl3 = Label(window, text = "Time required")
    # lbl3.grid(row=10, column= 2)
    # lbl4 = Label(window, text = "Impact")
    # lbl4.grid(row=10, column= 3)
    # rowOffset = 20
    # rows = []
    # for i in range(5):
    #     cols = []
    #     for j in range(4):
    #         e = Entry(relief=GROOVE)
    #         e.grid(row=i+rowOffset, column=j, sticky=NSEW)
    #         e.insert(END, '%d.%d' % (i, j))
    #         cols.append(e)
    #     rows.append(cols)
    window.title('ToDo List')
    window.geometry("300x1200+10+10")
    window.mainloop()
def main():
    # createTodoListDummy()
    createUIForToDoList()

main()
