class Node: 
    def __init__(self, value, next=None): 
        self.value = value
        self.next = next 

    def print_list(self): 
        temp = self 
        while temp is not None: 
            print(temp.value, end="->")
            temp= temp.next 
        print()


def reverse(head): 
    prev = None 
    curr,nxt = head, head.next 
    while(True): 
        curr.next = prev 
        if (nxt is None): 
            break 
        prev= curr 
        curr = nxt
        nxt = nxt.next
    # curr.next = prev 


    return curr


def main(): 
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    head.print_list()

    result =  reverse(head)

    result.print_list()

main()