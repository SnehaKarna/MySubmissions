class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        old_to_new = {}

        def dfs(node):

            # Already cloned this node
            if node in old_to_new:
                return old_to_new[node]

            # Create a copy of the current node
            copy = Node(node.val)

            # Store it BEFORE cloning neighbors
            old_to_new[node] = copy

            # Clone every neighbor
            for neighbor in node.neighbors:

                cloned_neighbor = dfs(neighbor)

                # Connect cloned neighbor to cloned node
                copy.neighbors.append(cloned_neighbor)

            return copy

        return dfs(node)