from typing import List

class Solution(object):
    """
    Implement atoi, which converts a string to integer.
    The function first discards as many whitespaces characters until the first non-whitespace character is found.
    Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
    digits as possible, and interprets them as a numerical value.
    The string can contain additional characters after those that form the integer number, which are ignored and have
    no effect on the behavior of this function.
    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
    exists because either str is empty or it contains only whitespace characters, no conversion is performed.
    If no valid conversion could be performed, a zero value is returned.
    """
    @staticmethod
    def atoi(str: str) -> int:
        str = str.strip()

        if not str:
            return 0

        negative = False
        out = 0

        if str[0] == "-":
            negative = True
        elif str[0] == "+":
            negative = False
        elif not str[0].isnumeric:
            return 0
        else:
            out = ord(str[0]) - ord("0")

        for i in range(1, len(str)):
            if str[i].isnumeric():
                out = out*10 + (ord(str[i]) - ord("0"))
                if not negative and out >= 2147483647:
                    return 2147483647
                if negative and out >= 2147483647:
                    return -2147483647
            else:
                break

        if not negative:
            return out
        else:
            return -out

if __name__ == '__main__':
    input = "45t6 gf"

    output = Solution.atoi(input)

    print(f"Output is: {output}")

