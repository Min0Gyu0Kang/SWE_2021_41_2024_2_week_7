from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Create a dictionary to store the value and index
    num_map = {}
    
    # Iterate over the array
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_map:
            return [num_map[complement], i]
        
        # Otherwise, store the index of the current number
        num_map[num] = i

    return []  # Return an empty list if no solution is found
'''
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
'''
'''
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
'''
'''
Input: nums = [3,3 ], target = 6
Output: [0, 1]
'''
