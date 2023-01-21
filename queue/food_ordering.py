from collections import deque
import time
import threading

orders_list=['pizza','burger','biriyani','rice']

class Food_Orders:
    def __init__(self):
        self.orders=deque()
        
    def order_food(self):
        for item in orders_list:
            time.sleep(0.5)
            self.orders.appendleft(item)
            print(item)

    def place_order(self):
        for item in self.orders:
            time.sleep(2)
            print(self.orders.popleft())
    
if __name__=='__main__':
    ff=Food_Orders()
    t1=threading.Thread(target=ff.order_food)
    t2=threading.Thread(target=ff.place_order)
    t1.start()
    t2.start()

    
