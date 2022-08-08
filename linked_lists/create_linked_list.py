class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_list:
    def __init__(self):
        self.head=None
        
    def insert_in_head(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def display_node(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            data=self.head
            while data:
                print(data.data)
                data=data.next
                

if __name__=='__main__':
    ll=Linked_list()
    ll.insert_in_head(5)
    ll.insert_in_head(10)
    ll.display_node()