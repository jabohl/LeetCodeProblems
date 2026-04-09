class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elementDictionary={}
        for index in nums:
            elementDictionary[index] = []
            
        for index in range(len(nums)):
            elementDictionary[nums[index]].append(index)
        
        listOfElements=[]
        
        for val in myDict:
        
            if len(elementDictionary[val]) > len(nums) / 3:
            
                listOfElements.append(val)
        
        return listOfElements
