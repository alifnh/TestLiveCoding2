class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node
    
    def printLL(self):
        current_node = self.head
        list_ll = []
        while(current_node):
            list_ll.append(current_node.data)
            current_node = current_node.next
        print(list_ll)

def sum2LinkedList(ll1, ll2):

    result_ll = LinkedList()
    penambah = 0
    current_node1 = ll1.head
    current_node2 = ll2.head

    while current_node1 or current_node2 or penambah:
        bil1 = current_node1.data if current_node1 else 0
        bil2 = current_node2.data if current_node2 else 0

        jum = bil1 + bil2 + penambah
        penambah = jum // 10
        jum = jum % 10
        result_ll.insertAtEnd(jum)

        current_node1 = current_node1.next if current_node1 else None
        current_node2 = current_node2.next if current_node2 else None
        

    return result_ll
        

# Test Case 1
llist1 = LinkedList()
llist1.insertAtEnd(2)
llist1.insertAtEnd(3)

llist2 = LinkedList()
llist2.insertAtEnd(5)
llist2.insertAtEnd(2)

test1 = sum2LinkedList(llist1, llist2)

print('Test 1')
print('Input: ')
llist1.printLL()
llist2.printLL()
print('Output: ')
test1.printLL()

# Test Case 2
llist1 = LinkedList()
llist1.insertAtEnd(2)
llist1.insertAtEnd(4)
llist1.insertAtEnd(3)

llist2 = LinkedList()
llist2.insertAtEnd(5)
llist2.insertAtEnd(6)
llist2.insertAtEnd(4)

test1 = sum2LinkedList(llist1, llist2)

print('Test 2')
print('Input: ')
llist1.printLL()
llist2.printLL()
print('Output: ')
test1.printLL()