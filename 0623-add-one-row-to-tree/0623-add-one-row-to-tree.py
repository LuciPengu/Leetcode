# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        stack = [root]
        temp = stack
        level = 1
        if depth == 1:
            rootNode = TreeNode(val)
            rootNode.left = root
            return rootNode
        while True:
            temp = []
            print(level, "HERE")
            if level == depth-1:
                for node in stack:
                    if node:
                        print(node.val)
                    
                        leftNode = TreeNode(val)
                        leftNode.left = node.left
                        node.left = leftNode
                        
                        rightNode = TreeNode(val)
                        rightNode.right = node.right
                        node.right = rightNode
                return root
                        
                        
            for node in stack:
                if node:
                    temp.append(node.left)
                    temp.append(node.right)
            stack = temp
            level += 1
        return root