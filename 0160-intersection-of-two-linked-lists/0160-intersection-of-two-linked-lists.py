class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        while pA != pB:
            # when A reaches end, jump to B
            pA = pA.next if pA else headB
            
            # when B reaches end, jump to A
            pB = pB.next if pB else headA

        return pA  # intersection node or None