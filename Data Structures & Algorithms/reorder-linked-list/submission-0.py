# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return 
        
        nums = []
        node = head
        nums.append(node)
        while node.next != None:
            node = node.next
            nums.append(node)
        l = len(nums) - 1

        i = 0
        j = l
        while i < j:
            nums[i].next = nums[j]
            i += 1
            if i >= j:
                break
            nums[j].next = nums[i]
            j -= 1

        nums[i].next = None