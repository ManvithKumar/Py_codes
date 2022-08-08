import time


def bubblesort(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]    
    return elements              

 
elements = [39, 12, 18, 85, 72, 10, 2, 18]

start=time.time()
print(start)
bubblesort(elements)
print(elements)
end=time.time()
print(end)
