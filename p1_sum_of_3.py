from typing import List


class Solution(object):
    """
    Given an array nums of n integers, are there 3 elements that sum up to 0 (exclude duplicate pairs)?
    [-1, -, 1, 2, -1, -4] Take one element in the array and see if there are other 2 elements that sum up to 0
    We will take 2 pointers: Left and Right and sort the array in the ascending order.
    If the sum of 3 is less than 0, we shift the Left pointer to right, otherwise we shift the Right pointer
    If the sum of 3 is equal to 0, we increase Left and decrease Right
    """
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        length = len(nums)

        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = length - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l = l + 1
                elif total > 0:
                    r = r - 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # now check for consecutive duplicates:
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r-1]:
                        r = r - 1

                    l = l + 1
                    r = r - 1

        return res


if __name__ == '__main__':
    input = [-1, 0, 1, 2, -1, -4]

    output = Solution.threeSum(input)

    print(f"Output is: {output}")