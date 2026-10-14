#```python
# Task 3: Python Problem-Solving Practice


from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating,
    are_anagrams,
    first_repeating,
    move_zeros,
    second_highest,
    remove_duplicates,
    missing_number,
    two_sum,
    closest_to_zero,
    common_elements,
    rotate_right,
    max_consecutive_sum,
    all_target_pairs
)

# Q1: Find the Frequency of Each Word
print("\nQ1: Word Frequency")
print("Example:", word_frequency("python is easy and python is powerful"))
print("Additional:", word_frequency("hi hi bye"))

# Q2: Find the Frequency of Each Character
print("\nQ2: Character Frequency")
print("Example:", character_frequency("banana"))
print("Additional:", character_frequency("book"))

# Q3: First Non-Repeating Character
print("\nQ3: First Non-Repeating Character")
print("Example:", first_non_repeating("aabbc"))
print("Additional:", first_non_repeating("hello"))

# Q4: Check Whether Two Strings Are Anagrams
print("\nQ4: Anagrams")
print("Example:", are_anagrams("listen", "silent"))
print("Additional:", are_anagrams("hello", "world"))

# Q5: First Repeating Character
print("\nQ5: First Repeating Character")
print("Example:", first_repeating("abca"))
print("Additional:", first_repeating("hello"))

# Q6: Move All Zeros to the End
print("\nQ6: Move Zeros")
print("Example:", move_zeros([0, 1, 0, 3, 12]))
print("Additional:", move_zeros([4, 0, 2, 0, 1]))

# Q7: Second Highest Distinct Number
print("\nQ7: Second Highest")
print("Example:", second_highest([10, 5, 8, 10, 3]))
print("Additional:", second_highest([1, 2, 3]))

# Q8: Remove Duplicates Without Changing Order
print("\nQ8: Remove Duplicates")
print("Example:", remove_duplicates([1, 2, 2, 3, 1, 4]))
print("Additional:", remove_duplicates([5, 5, 6, 7, 6]))

# Q9: Find the Missing Number from 1 to N
print("\nQ9: Missing Number")
print("Example:", missing_number([1, 2, 4, 5], 5))
print("Additional:", missing_number([1, 3, 4, 5], 5))

# Q10: Two Numbers Whose Sum Equals Target
print("\nQ10: Two Sum")
print("Example:", two_sum([2, 7, 11, 15], 9))
print("Additional:", two_sum([3, 2, 4], 6))

# Q11: Number Closest to Zero
print("\nQ11: Closest to Zero")
print("Example:", closest_to_zero([-4, -2, 1, 4, 8]))
print("Additional:", closest_to_zero([-5, 3, 2]))

# Q12: Common Elements Between Two Lists
print("\nQ12: Common Elements")
print("Example:", common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print("Additional:", common_elements([5, 6, 7], [6, 7, 8]))

# Q13: Rotate a List to the Right by K Positions
print("\nQ13: Rotate List")
print("Example:", rotate_right([1, 2, 3, 4, 5], 2))
print("Additional:", rotate_right([10, 20, 30], 1))

# Q14: Maximum Sum of Two Consecutive Elements
print("\nQ14: Maximum Consecutive Sum")
print("Example:", max_consecutive_sum([1, 2, 3, 4]))
print("Additional:", max_consecutive_sum([5, 1, 8, 2]))

# Q15: All Pairs Whose Sum Equals Target
print("\nQ15: All Target Pairs")
print("Example:", all_target_pairs([1, 2, 3, 4, 5], 6))
print("Additional:", all_target_pairs([2, 4, 1, 5, 3], 6))
