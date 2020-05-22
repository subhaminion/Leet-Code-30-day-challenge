#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#Example 1:
#Input: [2,2,1]
#Output: 1

#Example 2:
#Input: [4,1,2,1,2]
#Output: 4


#Approach 1: We use hash table to avoid the O(n)O(n) time required for searching the elements.
#Iterate through all elements in nums and set up key/value pair.
#Return the element which appeared only once.

#Complexity Analysis
#Time complexity : O(n * 1) = O(n). Time complexity of for loop is O(n)
#Time complexity of hash table(dictionary in python) operation pop is O(1)O(1).
#Space complexity : O(n). The space required by hash_table is equal to the number of elements in 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        hash_table = hash_table.fromkeys(nums, 0)
        
        for num in nums:
            hash_table[num] = hash_table[num] + 1
        for key in hash_table:
            if hash_table[key] == 1:
                return key
    
