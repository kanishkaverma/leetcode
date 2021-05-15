
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_cycle_length(self, head: ListNode):
        if head == None or head.next == None:
            return -1
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return self.get_cycle_length_helper(slow)
        return -1

    def get_cycle_length_helper(self, slow):
        pointer1 = slow
        pointer2 = slow
        length = 0
        while True:
            length += 1
            pointer2 = pointer2.next
            if (pointer1 == pointer2):
                print('break')
                break

        return length

    def detectCycle(self, head: ListNode) -> ListNode:
        cycle_length = self.get_cycle_length(head)

        if cycle_length == -1:
            return None

        else:
            pointer1, pointer2 = head, head
            print(cycle_length)
            for i in range(0, cycle_length):
                pointer2 = pointer2.next
            while True:
                if pointer1 == pointer2:
                    return pointer1
                pointer1 = pointer1.next
                pointer2 = pointer2.next


def main():

    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = None
    head.next.next.next.next = head.next

    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = head

    sol1 = Solution()

    print(sol1.detectCycle(head))

    # print(sol1.)


main()
