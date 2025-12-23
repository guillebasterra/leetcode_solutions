# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #given the root of a binary tree
        # return the level order traversal of its nodes values
        # so input
        #    3
        #.  / \
        #. 4. 20
        # return [[3], [4,20]]
        # root can be None
        # -1000,1000
        # recursive solution, be checking the left and right subtrees for each node
        #bfs solution: queue, iterative
        if not root: return []
        res = []
        q = deque()
        q.append(root)
        level = 0
        while q:

            level_size = len(q)
            curr_level = []
            for i in range(level_size):
                curr = q.popleft()
                curr_level.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            res.append(curr_level)

        
        return res



        
