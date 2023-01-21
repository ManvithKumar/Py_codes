from collections import deque

class Queue:
    def __init__(self):
        self.queue=deque()
    
    def insert_into_queue(self,val):
        self.queue.appendleft(val)

    def display_queue(self):
        for data in self.queue:
            print(data)
        
    def delete_item(self):
        self.queue.popleft()


if __name__=='__main__':
    qq=Queue()
    qq.insert_into_queue(45)
    qq.insert_into_queue(40)
    qq.insert_into_queue(50)
    qq.insert_into_queue(12)
    qq.display_queue()
    qq.delete_item()
    print('---------------------------')
    qq.display_queue()

