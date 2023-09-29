class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        print("="*50)
        print("LINKED LIST OF MONTHS")
        print("="*50)
        val = self.head
        while val: # while self.head is not None
            print(val.data, end=" ")
            val = val.next

if __name__ == "__main__":
    linked_list = LinkedList()

    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    nodes = []
    for i in range(len(months)):
         nodes.append(Node(months[i]))
    
    linked_list.head = nodes[0]
    nodes[0].next = nodes[6]
    nodes[6].next = nodes[9]
    nodes[9].next = nodes[11]
    nodes[11].next = nodes[1]
    nodes[1].next = nodes[8]
    nodes[8].next = nodes[4]
    nodes[4].next = nodes[7]
    nodes[7].next = nodes[10]
    nodes[10].next = nodes[3]
    nodes[3].next = nodes[2]
    nodes[2].next = nodes[5]
    
    linked_list.print_list()