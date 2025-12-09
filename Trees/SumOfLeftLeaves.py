# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        lefts, nodeList,testList=[],[],[[root]]
        i,sum=0,0
        while len(testList[i]) > 0:
            myList=[]
            for index2 in range(len(testList[i])):   
                if testList[i][index2].left is not None:
                    lefts.append(testList[i][index2].left)
                    myList.append(testList[i][index2].left)
                if testList[i][index2].right is not None:
                    myList.append(testList[i][index2].right)
            testList.append(myList)
            i+=1
        for i in range(len(lefts)):
            if lefts[i].left is None and lefts[i].right is None:
                sum+=lefts[i].val
        return sum
