class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_list:
    def __init__(self):
        self.head=None
        
    #inserting the nodes from the head

    def insert_in_head(self,data):
        node=Node(data,self.head)
        self.head=node

    #inserting the nodes in the end of the linked list:

    def insert_in_tail(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return 0
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data,None)
    
    
    #For displaying the nodes
    def display_node(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            data=self.head
            while data:
                print(data.data)
                data=data.next
    
    #inserting multiple values:
    def inserting_many_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_in_tail(data)

    #measure the length of the linked list:
    def count_length(self):
         if self.head is None:
                print("Empty Linked List")
         else:
            data=self.head
            count=0
            while data:
                count+=1
                data=data.next
            print(count)


if __name__=='__main__':
    ll=Linked_list()
    ll.inserting_many_values(["goku","vegeta","broly","caulifa","gohan"])
    ll.count_length()
    ll.display_node()