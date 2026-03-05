import random
class Solution:

    def __init__(self, nums: List[int]):
    
        self.myList=[]
        self.resList=[]
        
        for val in nums:
            
            self.resList.append(val)
            self.myList.append(val)

    def reset(self) -> List[int]:
        
        self.myList=self.resList
        
        return self.myList

    def shuffle(self) -> List[int]:
        shuffleArray = []
        
        for val in self.myList:
            shuffleArray.append(val)
        
        random.shuffle(shuffleArray)
        
        return shuffleArray

