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
            """
            Tuples are used to store multiple items in a single variable.

            Tuple is one of 4 built-in data types in Python used to store collections of data, 
            the other 3 are List, Set, and Dictionary, all with different qualities and usage.

            A tuple is a collection which is ordered and unchangeable.
            https://www.w3schools.com/python/python_tuples.asp#:~:text=%2C%20%22cherry%22)-,Tuple,which%20is%20ordered%20and%20unchangeable.
            """
            result[tuple(count)].append(s)

        return result.values()
            