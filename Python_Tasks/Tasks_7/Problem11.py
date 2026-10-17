
# Problem 11: Two Strings
# https://www.hackerrank.com/challenges/two-strings/problem

p = int(input())

for _ in range(p):
    s1 = set(input().strip())
    s2 = set(input().strip())

    print("YES" if s1.intersection(s2) else "NO")
