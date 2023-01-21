from collections import deque
from posixpath import split

class Stack:
    def __init__(self):
        self.stack=deque()
    
    def get_and_reverse_a_string(self,val):
        val=val[::-1]
        val=val.split(" ")
        for i in val:
            self.stack.append(i)
        return self.stack
    
if __name__=='__main__':
    ss=Stack()
    print(ss.get_and_reverse_a_string("Covid 19 is near"))