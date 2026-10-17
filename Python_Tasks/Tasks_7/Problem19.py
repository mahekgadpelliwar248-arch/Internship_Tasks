
# Problem 19: Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-strings/problem

s = input().strip()
n = int(input())
queries = [int(input()) for _ in range(n)]

weights = set()
previous = ""
current_weight = 0

for char in s:
    if char == previous:
        current_weight += ord(char) - ord("a") + 1
    else:
        current_weight = ord(char) - ord("a") + 1

    weights.add(current_weight)
    previous = char

for value in queries:
    print("Yes" if value in weights else "No")
