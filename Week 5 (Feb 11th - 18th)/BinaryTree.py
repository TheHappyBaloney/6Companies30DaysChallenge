# 331. Verify Preorder Serialization of a Binary Tree

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        items = preorder.split(",")
        for i, val in enumerate(items):
            if i>0 and not stack:
                return False
            if stack:
                stack[-1][1] -= 1
                if stack[-1][1] == 0:
                    stack.pop()
            if val != "#":
                stack.append([val, 2])
        return not stack

    
