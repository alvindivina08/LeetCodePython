class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # set left and right pointer to 1 and max number inside piles
        l, r = 1, max(piles)
        # set result to what ever max number of piles is
        res = r

        # while left is less than or equal to r
        while l <= r:
            # calculate the middle number 
            # by adding l + r divided by 2
            k = (l + r) // 2

            # set hours to 0
            hours = 0

            # now iterate through piles
            for p in piles:
                # calculate hours needed to eat each pile
                hours += math.ceil(p / k)

            # now if hours is less than or equal to h
            if hours <= h:
                # calculate the minimum of the current result and k
                res = min(res, k)
                # now move the r pointer to k - 1
                r = k - 1
            # if hours is not less than or equal to h
            else:
                # move the pointer l to k + 1
                l = k + 1

        return res
        
    
piles = [3,6,7,11] 
# result -> 4