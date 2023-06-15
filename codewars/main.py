from typing import List

def remove_duplicates(nums: List[int]) -> List[int]:
    result = []
    
    # Iterate over the list in reverse order
    for num in reversed(nums):
        # Check if the element is already in the result list
        if num not in result:
            # Add the element to the beginning of the result list
            result.insert(0, num)
    
    return result

# Example usage
nums = [3, 4, 6, 3, 4, 3]
result = remove_duplicates(nums)
print(result)  # Output: [4, 6, 3]