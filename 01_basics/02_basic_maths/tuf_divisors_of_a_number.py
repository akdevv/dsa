# Divisors of a Number
# https://takeuforward.org/plus/dsa/problems/divisors-of-a-number
# pattern: iterate up to √n, add each divisor and its pair (n // divisor)
# peeked: hint
# brute:   O(n) time, O(n) space - iterate 1..n, collect all divisors
# optimal: O(√n) time, O(n) space - iterate 1..√n, add divisor + paired divisor
#
# problem:
#   given an integer n, return all divisors of n in sorted order.
#   a divisor completely divides n (no remainder).
#
#   example:
#     n = 6 → [1, 2, 3, 6]
#     n = 8 → [1, 2, 4, 8]


from math import isqrt


def solve(n: int) -> list[int]:
    divisors_arr = []
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            divisors_arr.append(divisor)
        divisor += 1
    return divisors_arr


def optimal(n: int) -> list[int]:
    arr = []
    for divisor in range(1, isqrt(n) + 1):
        if n % divisor == 0:
            arr.append(divisor)
            if divisor != n // divisor:
                arr.append(n // divisor)
    return sorted(arr)


if __name__ == "__main__":
    answer = optimal(36)
    print(answer)
