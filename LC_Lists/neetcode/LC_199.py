# Definition for a binary tree node.
from collections import UserList
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> UserList[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)


        return res

# Driver code
if __name__ == "__main__":
    # Construct the binary tree
    #       1
    #      / \
    #     2   3
    #      \   \
    #       5   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.right = TreeNode(5)
    # root.right.right = TreeNode(4)

    # Create Solution object and print the right side view
    solution = Solution()
    right_view = solution.rightSideView(root)
    print(right_view)  # Expected Output: [1, 3, 4]