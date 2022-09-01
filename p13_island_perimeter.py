from typing import List


class Solution(object):
    """
    You are given a map in form of a 2D integer grid where 1 represents land and 0
    represents water.
    Grid cells are connected horizontally/vertically (not diagonally). This grid is
    completely surrounded by water, and there is exactly one island.
    The island doesn't have "lakes". The grid is rectangular, width and height don't
    exceed 100. Determine the perimeter of the island.
    Example:
        [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
         Output will be 16, the total number of edges of squares containing 1.
    """
    @staticmethod
    def island_perimeter(grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        result = 0
        inc = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    result += 4
                    inc += 1
                if i > 0 and grid[i-1][j] == 1:
                    result -= 1
                if j > 0 and grid[i][j-1] == 1:
                    result -= 1
        print(inc)
        return result


if __name__ == '__main__':
    input = [[0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0]]

    print(len(input[0]))
    print(input[1][1])

    output = Solution.island_perimeter(input)

    print(f"Perimeter is: {output}")
