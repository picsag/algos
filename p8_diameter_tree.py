from typing import List

class Solution(object):
    """
    Given a binary tree, you need to compute the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.
    The solution is:
            max(Left height+Right height, max(Left diameter, R diameter))
    """
    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:


if __name__ == '__main__':
    input = [[1,3], [2,6], [8,10], [15,18]]

    output = Solution.merge(input)

    print(f"Output is: {output}")