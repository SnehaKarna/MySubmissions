class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Dummy node helps us easily build the result list
        dummy = ListNode()

        # cur points to the last node in our result
        cur = dummy

        # Stores carry from the previous addition
        carry = 0

        # Continue while there is something left to add
        while l1 or l2 or carry:

            # Get l1's current value
            # If l1 is finished, use 0
            v1 = l1.val if l1 else 0

            # Get l2's current value
            # If l2 is finished, use 0
            v2 = l2.val if l2 else 0

            # Add the two digits + carry
            val = v1 + v2 + carry

            # Get the carry for the next digit
            carry = val // 10

            # Keep only the current digit
            val = val % 10

            # Create a node containing the current digit
            cur.next = ListNode(val)

            # Move cur to the newly created node
            cur = cur.next

            # Move l1 forward
            if l1:
                l1 = l1.next

            # Move l2 forward
            if l2:
                l2 = l2.next

        # Dummy itself is not part of the answer
        # The real answer starts at dummy.next
        return dummy.next