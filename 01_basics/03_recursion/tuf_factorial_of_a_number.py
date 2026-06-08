# 0004 - Factorial of a Number: Iterative and Recursive
# https://takeuforward.org/data-structure/factorial-of-a-number-iterative-and-recursive
# pattern: recursion
# peeked: no
# brute:   O(N) - iterative, multiply 1 to N
# optimal: O(N) time, O(N) space - recursive
#
# problem:
#   Given positive integer X, print X! = X*(X-1)*...*1
#
#   example:
#     X=5 → 120  (5*4*3*2*1)
#     X=1 → 1


def solve(n: int):
    if n == 0:
        return 1
    return n * solve(n - 1)


if __name__ == "__main__":
    answer = solve(3)
    print(answer)
