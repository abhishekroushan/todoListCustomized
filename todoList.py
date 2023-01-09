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

class TodoListItem(object):
    def __init__(self, item:str):
        self.item = item
        self.attributes = None
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
            print(i,":",l)

