# 0009 - Sum of First N Natural Numbers
# https://takeuforward.org/data-structure/sum-of-first-n-natural-numbers
# pattern: recursion
# peeked: no
# brute:   O(N) - recurse, add each number
# optimal: O(1) time, O(1) space - N*(N+1)/2 formula
#
# problem:
#   Given integer N, find sum of first N natural numbers using recursion.
#
#   example:
#     N=3 → 6  (1+2+3)
#     N=5 → 15 (1+2+3+4+5)


def solve(n: int):
    if n == 0:
        return 0
    return n + solve(n - 1)


def optimal(n: int):
    return (n * (n + 1)) // 2


if __name__ == "__main__":
    answer = optimal(5)
    print(answer)
