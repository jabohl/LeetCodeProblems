class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        if len(nums) < 2:
            return
        index = 0
        startPtr = 0
        endPtr = len(nums)-1
        while(index <= endPtr):
            if nums[index] == 0:
                
                temp = nums[startPtr]
                nums[startPtr] = nums[index]
                nums[index] = temp
                index += 1
                startPtr += 1
            elif nums[index] == 1:
                index += 1
            else:
                temp = nums[endPtr]
                nums[endPtr] = nums[index]
                nums[index] = temp
                endPtr -= 1
