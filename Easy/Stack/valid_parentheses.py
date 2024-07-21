class Solution:
    def isValid(self, s: str) -> bool:
        # map out the characters
        d = {'(':')','{':'}','[':']'}
        # create a stack
        stack = []

        # iterate through s string
        for i in s:
            print(f"Current character: {i}")
            print(f"Current stack: {stack}")

            # if current string is in map d
            if i in d:
                # add the current string in stack
                stack.append(i)
                print(f"Added {i} to stack. Stack is now: {stack}")
            # else if it's the right bracket and the stack is empty (meaning no matching
            # left bracket), or the left bracket doesn't match
            elif len(stack) == 0:
                print(f"Stack is empty when trying to match {i}. Returning False.")
                return False
            elif d[stack.pop()] != i:
                print(f"Top of stack doesn't match {i}. Returning False.")
                return False
        
        print(f"Final stack: {stack}")
        return len(stack) == 0
