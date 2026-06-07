# 0014 - Pattern 14
# https://takeuforward.org/plus/dsa/problems/pattern-14
# pattern: nested loops
# peeked: no
# brute:   O(n^2) - nested loops with chr()
# optimal: O(n^2) time, O(1) space - same, no better possible
#
# problem:
#   given an integer n, recreate the pattern below for any value of n.
#   for n=5:
#
#   A
#   AB
#   ABC
#   ABCD
#   ABCDE
#
#   print the pattern in the function given to you.
#   constraints: 1 <= n <= 26


def pattern14(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(i + 1):
            print(letters[j], end="")
        print()


def pattern14_better(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j), end="")
        print()


if __name__ == "__main__":
    pattern14_better(5)
