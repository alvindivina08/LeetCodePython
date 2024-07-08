from collections import defaultdict
from typing import List


class Solution:
    def getSignature(self, s:str) -> str:
        # creates an array of 26 zeros
        count = [0] * 26

        # first it will calculate the letter on where it will be placed in an array
        # for example letter a, ord('a') - ord('a') is 0
        # so it will be adding +1 to count[0]
        # adds +1 to the element 
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []

        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        print(''.join(result))
        return ''.join(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []

        groups = defaultdict(list)


        for s in strs:
            groups[self.getSignature(s)].append(s)


        result.extend(groups.values())


        return result


# short solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)

        return result.values()
            