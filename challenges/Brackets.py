
def Brackets(str):
    stack = []
    closeToOpen = { ")":"(", "}" :"{", "]":"[" }
    for i in str:
        if i in closeToOpen:
            if  stack and stack[-1] == closeToOpen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False

str='{[()]}'
if Brackets(str):
     print('Valid')
else:
    print('invalid')