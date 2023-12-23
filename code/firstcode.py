def isMonotonic(nums):
    if not (1 <= len(nums) <= 10**5):
        raise ValueError("Length of nums is out of bounds.")
    
    for num in nums:
        if not (-10**5 <= num <= 10**5):
            raise ValueError("Value in nums is out of bounds.")
    
    increasing = decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        elif nums[i] < nums[i - 1]:
            increasing = False
            
    return increasing or decreasing

# Test cases
nums1 = list(input().split())
print(isMonotonic(nums1))  # Output: True

# nums2 = [6, 5, 4, 4]
# print(isMonotonic(nums2))  # Output: True

# nums3 = [1, 3, 2]
# print(isMonotonic(nums3))  # Output: False
