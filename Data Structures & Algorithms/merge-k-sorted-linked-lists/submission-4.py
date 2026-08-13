class Solution:
    def mergeKLists(self, lists):

        if not lists:
            return None

        def merge(l1, l2):
            dummy = ListNode()
            cur = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next

                cur = cur.next

            if l1:
                cur.next = l1
            else:
                cur.next = l2

            return dummy.next

        interval = 1

        while interval < len(lists):

            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])

            interval *= 2

        return lists[0]