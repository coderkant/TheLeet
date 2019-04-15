class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Solution using a python dict
        space - O(n)
        time - O(n)
        Runtime: 44 ms, faster than 57.46% of Python3 online submissions for Two Sum.
        Memory Usage: 14.7 MB, less than 5.08% of Python3 online submissions for Two Sum.
        '''
        tempDict = {}
        for i, x in enumerate(nums):
            loc2 = tempDict.get(str(x), -1)
            if loc2 != -1:
                return loc2, i
            else:
                tempDict.update({str(target - x): i})