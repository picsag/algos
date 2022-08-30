from typing import List

class Solution(object):
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which
    has the largest sum and return its sum.
    """
    @staticmethod
    def max_sub_array(nums: List[int]) -> List[int]:
        total_sum = max_sum = nums[0]

        for i in nums[1:]:
            total_sum = max(i, total_sum + i)
            max_sum = max(max_sum, total_sum)

        return max_sum


if __name__ == '__main__':
    input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    output = Solution.max_sub_array(input)

    print(f"Output is: {output}")