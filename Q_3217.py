class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        arr = set(nums)
        temp = ListNode(0,head)
        head = temp

        while temp.next:
            if temp.next.val in arr:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head.next

        
