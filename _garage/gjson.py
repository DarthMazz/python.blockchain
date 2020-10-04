import json

class Block:
    """A simple example class"""
    
    def __init__(self):
        self.name = ""
    def getName(self):                   # getName()メソッド
        return self.name
    def setName(self, name):             # setName()メソッド
        self.name = name


block = Block()
print(block.getName())

print(json.dumps(block, sort_keys=True))
