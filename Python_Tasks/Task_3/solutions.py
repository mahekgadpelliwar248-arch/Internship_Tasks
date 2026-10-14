# Q1: Find the Frequency of Each Word in a Sentence

def word_frequency(sentence):
    frequency = {}

    for word in sentence.split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Q2: Find the Frequency of Each Character in a Word

def character_frequency(word):
    frequency = {}

    for char in word:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency

# Q3: Find the First Non-Repeating Character in a Word

def first_non_repeating(word):
    frequency = {}

    for char in word:
        frequency[char] = frequency.get(char, 0) + 1

    for char in word:
        if frequency[char] == 1:
            return char

    return None

# Q4: Check Whether Two Strings Are Anagrams

def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)

# Q5: Find the First Repeating Character in a String

def first_repeating(string):
    seen = set()

    for char in string:
        if char in seen:
            return char

        seen.add(char)

    return None

# Q6: Move All Zeros to the End of a List

def move_zeros(nums):
    non_zeros = []
    zeros = []

    for num in nums:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)

    return non_zeros + zeros

# Q7: Find the Second Highest Distinct Number in a List

def second_highest(nums):
    unique_nums = sorted(set(nums), reverse=True)

    if len(unique_nums) < 2:
        return None

    return unique_nums[1]

# Q8: Remove Duplicates Without Changing the Original Order

def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result

# Q9: Find the Missing Number from 1 to N

def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum

# Q10: Find Two Numbers Whose Sum Equals a Target

def two_sum(nums, target):
    seen = []

    for num in nums:
        needed = target - num

        if needed in seen:
            return [needed, num]

        seen.append(num)

    return []

# Q11: Find the Number Closest to Zero

def closest_to_zero(nums):
    if not nums:
        return None

    return min(nums, key=lambda num: (abs(num), -num))

# Q12: Find Common Elements Between Two Lists

def common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result

# Q13: Rotate a List to the Right by K Positions

def rotate_right(nums, k):
    if not nums:
        return []

    k = k % len(nums)

    return nums[-k:] + nums[:-k] if k else nums[:]

# Q14: Find the Maximum Sum of Two Consecutive Elements

def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Q15: Find All Pairs of Numbers Whose Sum Equals a Target

def all_target_pairs(nums, target):
    pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in pairs:
                    pairs.append(pair)

    pairs.sort(key=lambda pair: pair[0])

    return pairs

