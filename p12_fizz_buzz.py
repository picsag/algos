from typing import List


class Solution(object):
    """
        Write a program that outputs the string representation of numbers from 1 to n.
        But for multiples of 3 it should output Fizz instead of the number and for multiples of 5
        it should output "Buzz". For numbers which are multiples of both 3 and 5 output "FizzBuzz".
    """
    @staticmethod
    def fizz_buzz(n: int) -> List[str]:
        fizz_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                fizz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_list.append("Fizz")
            elif i % 5 == 0:
                fizz_list.append("Buzz")
            else:
                fizz_list.append(str(i))
        return fizz_list


if __name__ == '__main__':

    output = Solution.fizz_buzz(16)

    print(f"Output is: {output}")
