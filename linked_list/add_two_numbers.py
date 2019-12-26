# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:         
        sum_int = self.getSum(l1, -1) + self.getSum(l2, -1)
        output = self.makeLinkedList(reversed(str(sum_int)))
        return output
            
    def makeLinkedList(self, inputs):
        try:
            next_input = next(inputs)
        except StopIteration:
            return None
        node = ListNode(next_input)
        node.next = self.makeLinkedList(inputs)
        
        return node
    
    def getSum(self, node, magnitude):
        if node == None:
            return 0
        magnitude += 1
        this_node = (node.val * 10 ** magnitude)
        next_node = self.getSum(node.next, magnitude)
        return this_node + next_node
