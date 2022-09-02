from typing import List


class Solution(object):
    """
    Balanced strings are those who have equal quantity of 'L' and 'R' characters
    Given a balanced string s split it in the maximum amount of balanced strings
    Return the maximum amount of split balanced strings.
    Example: "RLRRRLLRLL" has 2 sequences: RL and RRRLLRLL
    """
    @staticmethod
    def balanced_strings(s: str) -> int:
        counter = 0
        r = 0
        for i in range(0, len(s)):
            if s[i] == 'R':
                r += 1
            if s[i] == 'L':
                r -= 1
            if r == 0:
                counter += 1
        return counter


if __name__ == '__main__':
    input = "RLRRRLLRLLRLLR"  # correct answer is 4

    output = Solution.balanced_strings(input)

    print(f"Output is: {output}")
