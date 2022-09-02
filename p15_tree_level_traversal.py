from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    Given a binary tree, return the level order traversal of its nodes' values,
    i.e. from left to right, level by level.
    Example:  3
            /   \
           9     20
          / \   /  \
               15   7
    The output will be a list of elements for each level: [3, [9, 20], [15, 7] ]
    """
    @staticmethod
    def level_order_traversal(root: TreeNode) -> List[List[int]]:
        if root is None:
            return

        # Enqueue Root
        queue = [root]

        while len(queue) > 0:
            # Print front of queue and remove it from queue
            print(queue[0].val)
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)


if __name__ == '__main__':
    # Driver Program to test above function
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    output = Solution.level_order_traversal(root)

