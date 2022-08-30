class Solution(object):
    """
    Given a string, return the length of the longest substring without repeating characters
    """
    @staticmethod
    def length_of_longest_substring(s: str) -> int:

        if len(s) == 0:
            return 0

        map = {}  # dictionary holding a character as key and index in string as value

        max_length = 0 # maximum length of substring starting from a character
        start = 0

        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            map[s[i]] = i
        return max_length


if __name__ == '__main__':
    input = 'abcabcbb'

    output = Solution.length_of_longest_substring(input)

    print(f"Output is: {output}")