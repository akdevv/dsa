# 0013 - Pattern 13
# https://takeuforward.org/plus/dsa/problems/pattern-13
# pattern: nested loops
# peeked: no
# brute:   O(n^2) - nested loops with running counter
# optimal: O(n^2) time, O(1) space - same, no better possible
#
# problem:
#   given an integer n, recreate the pattern below for any value of n.
#   for n=5:
#
#   1
#   2 3
#   4 5 6
#   7 8 9 10
#   11 12 13 14 15
#
#   print the pattern in the function given to you.


def pattern13(n):
    count = 1
    for i in range(n):
        for _ in range(i + 1):
            print(count, end=" ")
            count += 1
        print()


if __name__ == "__main__":
    pattern13(5)
