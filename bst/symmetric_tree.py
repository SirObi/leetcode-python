# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        is_symmetric = True
        buffer = [root]
        
        while any(buffer) and is_symmetric == True:
            values = [node.val if node != None else None for node in buffer]
            is_symmetric = values == values[::-1]
            new_buffer = []
            for node in (n for n in buffer if n != None):
                new_buffer.append(node.left)
                new_buffer.append(node.right)
            buffer = new_buffer
        return is_symmetric
