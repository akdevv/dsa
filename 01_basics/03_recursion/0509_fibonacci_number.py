# 0509 - Fibonacci Number
# https://leetcode.com/problems/fibonacci-number
# pattern: recursion, F(n) = F(n-1) + F(n-2) with base cases
# peeked: no
# brute:   O(2^n) time, O(n) space - recursive calls, stack depth n
#
# problem:
#   Given n, return F(n) where F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
#
#   example:
#     2 → 1
#     3 → 2
#     4 → 3


def solve(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return solve(n - 1) + solve(n - 2)


if __name__ == "__main__":
    answer = solve(10)
    print(answer)
