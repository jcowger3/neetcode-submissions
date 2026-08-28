# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return 
        
        nums = []
        node = head
        nums.append(node.val)
        while node.next != None:
            node = node.next
            nums.append(node.val)
        
        r_nums = reversed(nums)

        node = ListNode()
        re_head = ListNode(next = node)
        for i, num in enumerate(r_nums):
            node.val = num

            if i < len(nums)-1:
                node.next = ListNode()
                node = node.next
        
        return re_head.next


        