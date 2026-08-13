class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):

            # Both empty → same
            if not p and not q:
                return True

            # Only one is empty → different structure
            if not p or not q:
                return False

            # Values are different
            if p.val != q.val:
                return False

            # Compare left AND right subtrees
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)