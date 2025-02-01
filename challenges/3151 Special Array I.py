"""An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

 

Example 1:

Input: nums = [1]

Output: true

Explanation:

There is only one element. So the answer is true.

Example 2:

Input: nums = [2,1,4]

Output: true

Explanation:

There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:

Input: nums = [4,3,1,6]

Output: false

Explanation:

nums[1] and nums[2] are both odd. So the answer is false.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
            """For this special array we have to loop through the array called nums that can contain one or more numbers
            1) Create the loop and the boundaries for the loop, the lenght of the array
            2) compare if the element number of the array is even or odd and compare it to the previous element in the array
            3) if both are even then it's not an special array
            4) if one is even and the other one isn't then it's an special array"""
            for num in range(1, len(nums)):
                if nums[num] % 2 ==  nums[num-1] % 2 :
                    return False
            return True