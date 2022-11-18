# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        swap = 0
        if head != None:
            while(1):

                swap = 0
                tmp = head
                while(tmp.next != None):
                    if tmp.val > tmp.next.val:
                        # swap them
                        swap += 1
                        p = tmp.val
                        tmp.val = tmp.next.val
                        tmp.next.val = p
                        tmp = tmp.next
                    else:
                        tmp = tmp.next

                if swap == 0:
                    break
                else:
                    continue



            return head
        else:
            return head