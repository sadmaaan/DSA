from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = None
        temp = head
        temp = self.reverseList(temp)
        
        # while temp and head:
        #     if head.val == temp.val:
        #         head = head.next
        #         temp = temp.next
        #     else:
        #         return False
        
        # return True
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        while head:
            print(head.val, end=" ")
            head = head.next
    
    def reverseList(self, node):
        if node is None or node.next is None:
            return node

        new_head = self.reverseList(node.next)
        node.next = None
    
        return new_head


sol = Solution()
x = ListNode(1, ListNode(2, ListNode(1, ListNode(1))))
# while x:
#     print(x.val)
#     x = x.next

s = sol.isPalindrome(ListNode(1, ListNode(2, ListNode(1, ListNode(1)))))
print(s)