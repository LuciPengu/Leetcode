class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        i = 0
        while queue:
            tempqueue = []
            values = set()
            prev = None
            for node in queue:
                if node.val % 2 == i % 2:
                    return False
                if node:
                    
                    if prev != None:
                        if i % 2 == 0:
                            if prev >= node.val:
                                return False
                        else:
                            if prev <= node.val:
                                return False
                            
                    if node.left:
                        tempqueue.append(node.left)
                        values.add(node.left.val)
                    
                    if node.right:
                        tempqueue.append(node.right)
                        values.add(node.right.val)
                    prev = node.val
                        
            
            queue = tempqueue
            i += 1
        
        return True