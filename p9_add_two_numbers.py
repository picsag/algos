
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    Given 2 numbers stored on 2 non-empty linked-lists, that hold on each node one digit. The digits are stored in
    reverse order. Add the two numbers and return the result as a linked list.
    Example: (1->4->3) + (2->6->3) = (3->0->7)
             341       + 362       = 703
    """
    @staticmethod
    def add_numbers(l1:ListNode, l2:ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        p = dummy
        while l1 or l2 or carry != 0:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            p.next = ListNode(carry % 10)
            carry //= 10
            p = p.next
        return dummy.next

    @staticmethod
    def display_list(l: ListNode):
        """
        Displays the number from the linked list stored in reverse order
        """
        value = 0
        level = 0
        while l.next:
            value += (10 ** level) * l.val
            level += 1
            l = l.next
        print(value)


if __name__ == '__main__':
    l1 = ListNode(1)
    p1 = l1
    l1.next = ListNode(4)
    l1 = l1.next
    l1.next = ListNode(3)
    l1 = l1.next
    l1.next = ListNode(0)

    l2 = ListNode(2)
    p2 = l2
    l2.next = ListNode(6)
    l2 = l2.next
    l2.next = ListNode(3)
    l2 = l2.next
    l2.next = ListNode(0)

    Solution.display_list(p1)

    Solution.display_list(p2)

    l3 = Solution.add_numbers(p1, p2)

    print("Sum =", end=' ')

    Solution.display_list(l3)

    # print(f"Output is: {output}")