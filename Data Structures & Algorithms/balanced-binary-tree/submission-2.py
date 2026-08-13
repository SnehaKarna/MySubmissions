class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            # Empty tree → height 0
            if not root:
                return 0

            # Get left subtree height
            left = dfs(root.left)

            # If left subtree is already unbalanced
            if left == -1:
                return -1

            # Get right subtree height
            right = dfs(root.right)

            # If right subtree is already unbalanced
            if right == -1:
                return -1

            # Check current node
            if abs(left - right) > 1:
                return -1

            # Return height
            return 1 + max(left, right)

        return dfs(root) != -1