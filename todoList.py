"""
Author: Abhishek Roushan (abhishek.roushan12@gmail.com)
Open source code for a cutom todo list solution
The user will be able to add fields, add attributes and 
sort them using different attributes
"""

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
            print(i,":", l.getItem(), "--", l.getAttributes())

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
    tl.print()

def main():
    createTodoListDummy()

main()
