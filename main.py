from typing import Optional


class Solution:
    def __init__(self) -> None:
        pass

    def reverse_string(string):
        return string[::-1]

    def reverse_using_for_loop(self, string):
        new_string = ""
        for i in range(len(string)-1,-1,-1):
            new_string += string[i]
        return new_string

    def sub_string(string):
        start = string.index("se ") + 3
        end = string.index(" str")
        new = string[start:end]
        return new

    def house_robber_ii(self, nums):
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[::-1]))
    
    def helper(self, nums):
        dp1, dp2 = 0, 0

        for n in nums:
            temp = max(n + dp1, dp2)
            dp1 = dp2
            dp2 = temp
        
        return dp2
    
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            a, b = s[i].lower(), s[j].lower()

            if a.isalnum() and b.isalnum():
                if a != b: return False
                i, j = i + 1, j - 1
                continue
            else:
                i, j = i + (not a.isalnum()), j - (not b.isalnum())
        
        return True
    
    def isValid(self, s: str) -> bool:
        d = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        
        return len(stack) == 0
    
    def reverse_linked_list(self, head:Optional[ListNode]) -> Optional[ListNode]:

        # 1 -> 2 -> 3 -> 4 -> 5 (head)
        # ^
        # prev
        # curr
        prev = None
        curr = head

        while curr:
            # next = 2, 3, 4, 5
            nxt = curr.next

            #  curr.next = prev
            # prev = 2, 3 , 4 ,5
            curr.next = prev

            # prev
            prev = curr
            curr = nxt
        return prev
    
test = Solution()

number = [1, 2, 3, 4]
this_string = "reverse this string!"
palindrome = "A man, a plan, a canal: Panama"
parentheses = "()[]{}"

yeet = test.reverse_using_for_loop(this_string)
isPalindrome = test.isPalindrome(palindrome)
houseRobber = test.house_robber_ii(number)
validParentheses = test.isValid(parentheses)

print(validParentheses)