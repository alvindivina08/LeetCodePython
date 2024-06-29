class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        
        while l < r:
            print(f"l = {l}, r = {r}")
            print(f"maxLeft = {maxLeft}, maxRight = {maxRight}")
            print(f"res = {res}")
            if maxLeft < maxRight:
                print("true")
                # update the left pointer
                l += 1
                # calculate the biggest number for maxLeft using max(maxLeft, height[l]) 
                maxLeft = max(maxLeft, height[l])
                # calculate the area by using maxLeft - height[l]
                res += maxLeft - height[l]
            else:
                print("false")
                # update the right pointer
                r -= 1
                # calculate the biggest number for maxRight using max(maxRight, height[r]) 
                maxRight = max(maxRight, height[r])
                # calculate the area by using maxRight - height[r]
                res += maxRight - height[r]
            
            print("\n")

        return res

# height = [0,1,0,2,1,0,1,3,2,1,2,1]

# l = 0, r = 11
# maxLeft = 0, maxRight = 1
# res = 0
# true


# l = 1, r = 11
# maxLeft = 1, maxRight = 1
# res = 0
# false


# l = 1, r = 10
# maxLeft = 1, maxRight = 2
# res = 0
# true


# l = 2, r = 10
# maxLeft = 1, maxRight = 2
# res = 1
# true


# l = 3, r = 10
# maxLeft = 2, maxRight = 2
# res = 1
# false


# l = 3, r = 9
# maxLeft = 2, maxRight = 2
# res = 2
# false


# l = 3, r = 8
# maxLeft = 2, maxRight = 2
# res = 2
# false


# l = 3, r = 7
# maxLeft = 2, maxRight = 3
# res = 2
# true


# l = 4, r = 7
# maxLeft = 2, maxRight = 3
# res = 3
# true


# l = 5, r = 7
# maxLeft = 2, maxRight = 3
# res = 5
# true


# l = 6, r = 7
# maxLeft = 2, maxRight = 3
# res = 6
# true


