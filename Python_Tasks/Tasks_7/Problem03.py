# Problem: Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
expected = "SOS"
count = 0

for i, char in enumerate(s):
    if char != expected[i % 3]:
        count += 1

print(count)
