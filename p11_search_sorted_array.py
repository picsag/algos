from typing import List


class Solution(object):
    """
    An array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    Example: [0, 0, 1, 2, 2, 5, 6] might become [2, 5, 6, 0, 0, 1, 2]
    If the pivot is found in the array return True otherwise False
    """
    @staticmethod
    def search_array(nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return True

            if nums[start] < nums[mid]:  # if first half of the array is sorted
                # if target is outside the limits of first half, reduce the search space to second half
                if target < nums[start] or target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[start] > nums[mid]:  # if first half of the array is not sorted
                # if target is outside the limits of second half, reduce the search space to first half
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                start += 1

        return False


if __name__ == '__main__':
    arr = [2, 5, 6, 0, 0, 1, 2]
    x = 0

    result = Solution.search_array(arr, x)

    if result:
        print(f"Element {x} is present: {str(result)}")
    else:
        print("Element is not present in array")