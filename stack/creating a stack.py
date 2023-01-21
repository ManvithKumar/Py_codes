from collections import deque

stack=deque()
stack.append(5)
stack.append(6)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(0)
stack.pop()

print(stack)