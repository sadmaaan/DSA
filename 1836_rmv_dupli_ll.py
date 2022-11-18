class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LL:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next  

    def insert_last(self, data):
        temp = self.head

        while temp.next:
            temp = temp.next
        
        temp_node = Node(data)
        temp.next = temp_node
    
    def rmv_dupli(self):
        h = {}
        temp = self.head

        while temp:
            if temp.data in h:
                h[temp.data] += 1
            else:
                h[temp.data] = 1
            temp = temp.next

        pred = Node(-1, self.head)
        prev = pred

        while self.head:
            if h.get(self.head.data) > 1:
                prev.next = self.head.next
            else:
                prev = prev.next
            
            self.head = self.head.next
        
        return pred.next       


if __name__ == '__main__':
    ll = LL()
    ll.head = Node(3)
    ll.insert_last(2)
    ll.insert_last(2)
    ll.insert_last(1)
    ll.insert_last(3)
    ll.insert_last(2)
    ll.insert_last(4)
    ll.print_LL()
    x = ll.rmv_dupli()
    print("\n")
    while x:
        print(f"{x.data}", end=" -> ")
        x = x.next
    