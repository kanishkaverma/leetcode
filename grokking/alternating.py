# given a linked list , rever alternate nodes and append to the end
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        # out= ''
        # node = self
        # while (node):
        #     out += str(node.val) + '-> '

        #     node = node.next
        # return out

        return str(self.val)


class solution:

    def make_list(self, head):
        head1 = head
        head2 = head.next
        node = head
        nxt_node = head.next
        nxt_nxt_node = head.next.next
        while(nxt_nxt_node):
            print(node, nxt_node, nxt_nxt_node)
            node.next = nxt_node.next
            nxt_node.next = nxt_nxt_node.next
            node = nxt_nxt_node
            nxt_node = nxt_nxt_node.next

            nxt_nxt_node = nxt_nxt_node.next.next 

            # print(node, nxt_node, nxt_nxt_node)

        return [head1, head2]

    def main(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = (ListNode(3))
        head.next.next.next = (ListNode(4))
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(6)
        node = head
        while (node): 
            print(node.val, end= '')

            node = node.next 

        head1 = self.make_list(head)[0]
        head2 = self.make_list(head)[1]
        node = head1
        while (node): 
            print(node.val, end= '')

            node = node.next
        print("    ")
        node = head2
        while (node): 
            print(node.val, end= '')

            node = node.next

Sol = solution()
Sol.main()
