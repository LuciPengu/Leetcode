# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def checkPseudoPalindrome(count):
            oddcount = 0
            total = 0
            for i in count:
                if count[i] % 2 != 0:
                    oddcount += 1
                total += count[i]
            
            if total % 2 != 0:
                return oddcount == 1
            else:
                return oddcount == 0
        
        res = 0
        def dfs(node, count):
            nonlocal res
            if node == None:
                return 0
            
            count[node.val] += 1
            
            if node.left == None and node.right == None:
                res += (checkPseudoPalindrome(count))
                
            dfs(node.left, count)
            dfs(node.right, count)
            
            count[node.val] -= 1
            
        count = defaultdict(int)

        dfs(root, count)
        return res