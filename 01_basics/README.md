# Basics

Striver A2Z — Step 1. Solve top-to-bottom, drop solutions as `NNNN_name.py`.

---

## Euclid's Algorithm

efficient way to find GCD (greatest common divisor) of two numbers.

GCD of two integers (a > b) equals GCD of b and the remainder of a divided by b.

`gcd(a, b) = gcd(b, a % b)` — repeat until b = 0, then a is the GCD.

---

## Recursion

recursion is when a function calls itself to solve a smaller version of the same problem.

- **base case:** the condition that stops the calls.
- **recursive case:** where the function calls itself with a smaller/modified argument.

each call adds a frame to the call stack. no base case = stack overflow.

e.g. fibonacci series. see `03_recursion/` for practice problems.

---

## Hashing

hashing is pre-computing and storing values so lookups are O(1) instead of O(n).

**frequency array:** when elements are in a known range (e.g. 0–10⁶), allocate an array of that size. `hash[x]` stores how many times `x` appears. O(n) build, O(1) query.

**hash map:** when elements are arbitrary (large values, strings, negatives), use a dict. same idea — store counts or presence keyed by value.

**core trade-off:** spend O(n) time and space up front, answer every query in O(1) after.

common uses:

- frequency count (`hash[x]++` while iterating)
- existence check (`x in hash`)
- first duplicate, most frequent element, pair/sum problems
