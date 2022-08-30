from typing import List

class Solution(object):
    """
    You have an array of logs. Each log is a space delimited string of words.
    For each log, the first word in each log is an alphanumeric identifier.
    Then, either:
    - each word after the identifier will consist only of lowercase letters
    - each word after the identifier will consist only of digits

    We will call these two varieties of logs letter-logs and digit-logs.
    Reorder the logs so that all of the letter-logs come before any digit-log. The letter-logs are ordered lexicographic
    ignoring the identifier, with the identifier used in case of ties. The digit-logs should be put in their original
    order
    Return the final order of the logs
    """
    @staticmethod
    def reorder_log_files(logs: List[str]) -> List[str]:
        res1, res2 = [], []
        for log in logs:
            if log.split()[1].isdigit():
                res2.append(log)
            else:
                res1.append(log.split())

        res1.sort(key=lambda x: x[0])
        res1.sort(key=lambda x: x[1:])

        for i in range(len(res1)):
            res1[i] = (" ".join(res1[i]))
        res1.extend(res2)
        return res1


if __name__ == '__main__':
    input = ['dig1 8151', "let1 art can", "dig2 3 6", "let 2 own kit dig", "let3 art zero"]

    output = Solution.reorder_log_files(input)

    print(f"Output is: {output}")