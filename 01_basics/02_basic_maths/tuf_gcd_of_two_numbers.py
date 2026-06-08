# GCD of Two Numbers
# https://takeuforward.org/plus/dsa/problems/gcd-of-two-numbers
# pattern: reduce problem using remainder till 0 (Euclid's algorithm)
# peeked: no
# brute:   O(n) time, O(n) space - find all divisors, intersect, take max
# optimal: O(log n) time, O(log n) space - GCD(a,b) = GCD(b, a%b) until b==0
#
# problem:
#   given two integers n1 and n2, return their greatest common divisor.
#   GCD is the largest positive integer that divides both numbers.
#
#   example:
#     n1 = 4, n2 = 6 → 2
#     n1 = 9, n2 = 8 → 1


def divisors(n: int):
    divisors_arr = []
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            divisors_arr.append(divisor)
        divisor += 1
    return divisors_arr


def solve(n1: int, n2: int) -> int:
    n1_divisors = divisors(n1)
    n2_divisors = divisors(n2)

    common_divisors = set(n1_divisors) & set(n2_divisors)
    return max(common_divisors)


def euclids_algorithm(n1: int, n2: int) -> int:
    if n2 == 0:
        return n1
    return euclids_algorithm(n2, n1 % n2)


if __name__ == "__main__":
    answer = euclids_algorithm(8, 4)
    print(answer)
