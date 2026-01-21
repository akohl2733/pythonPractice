class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


class Solution:

    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
    

    def invertTree(self, root):

        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
    

    def isValidBST(self, root: TreeNode) -> bool:
        
        def validate(node, min_val, max_val):

            if not node:
                return True
            
            if not (min_val < node.val < max_val):
                return False
            

            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))


from collections import deque

def print_tree(root):
    if not root:
        print("Empty tree.")
        return
    
    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    print(result)


sol = Solution()

print(sol.isValidBST(root))