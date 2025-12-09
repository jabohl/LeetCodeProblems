# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node=root
        smallList=[]
        smallList.append(node)
        if node.right is None and node.left is None:
            return False
        nodes=[node.val]
        while len(smallList) > 0:
            testList=[]
            
            tester=0
            
            for i in smallList:
                #if i.left is None and i.right is None:
                #    tester+=1
                
                if i.left is not None:
                    testList.append(i.left)
                    nodes.append(i.left.val)   
                if i.right is not None:
                    testList.append(i.right)
                    nodes.append(i.right.val)   
            
        
            smallList=testList
        
        for i in range(len(nodes)):
            
            if k-nodes[i] in nodes[i+1:] or k-nodes[i] in nodes[:i]:
                return True
        return False
