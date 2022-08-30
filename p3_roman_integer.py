class Solution(object):
    """
    Given a string, return the length of the longest substring without repeating characters
    """
    @staticmethod
    def roman_to_integer(s: str) -> int:
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        curr = 0
        prev = 0
        for i in range(len(s)):
            curr = dic[s[i]]
            if curr > prev:
                total = total + curr - 2 * prev
            else:
                total += curr
            prev = curr
        return total



if __name__ == '__main__':
    input = 'XXXIV'

    output = Solution.roman_to_integer(input)

    print(f"Output is: {output}")