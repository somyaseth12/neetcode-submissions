# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        # Dummy node helps handle the new head of the list
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 1. Find the kth node from group_prev
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            
            # 2. Reverse the group
            # 'prev' starts at group_next to link the reversed tail to the rest of the list
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 3. Connect the previous part of the list to the new head of this reversed group
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr