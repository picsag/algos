from typing import List


class Solution(object):
    """
    Binary search in a sorted array.
    It returns index of x in given array arr if present, else returns -1
    """
    @staticmethod
    def binary_search_recursive(nums: List[int], start: int, end: int, target: int) -> int:

        # Check base case
        if end >= start:

            mid = (end + start) // 2

            # If element is present at the middle itself
            if nums[mid] == target:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif nums[mid] > target:
                return Solution.binary_search_recursive(nums, start, mid - 1, target)

            # Else the element can only be present in right subarray
            else:
                return Solution.binary_search_recursive(nums, mid + 1, end, x)

        else:
            # Element is not present in the array
            return -1

    @staticmethod
    def binary_search(nums: List[int], target: int) -> int:
        start = 0
        end = len(arr) - 1
        mid = 0

        while start <= end:

            mid = (start + end) // 2

            # If x is greater, ignore left half
            if nums[mid] < x:
                start = mid + 1

            # If x is smaller, ignore right half
            elif nums[mid] > x:
                end = mid - 1

            # means x is present at mid
            else:
                return mid

        # If we reach here, then the element was not present
        return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 34, 39, 40, 70]
    x = 10

    # Function call
    result = Solution.binary_search_recursive(arr, 0, len(arr)-1, x)

    if result != -1:
        print(f"Element {x} is present at index {str(result)}")
    else:
        print("Element is not present in array")

    x = 39
    result = Solution.binary_search(arr, x)

    if result != -1:
        print(f"Element {x} is present at index {str(result)}")
    else:
        print("Element is not present in array")