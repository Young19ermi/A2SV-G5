class Solution:
    def partitionLabels(self, s: str) -> List[int]:
    
    #time complexity O(n)
    #Space complexity O(1)  
    #what we all need is build the hashmap that stores elements with the last index they found they iterate through the whole string if we found the next string in the index greater than the last index.
        lastindex = {}
        for i, char in enumerate(s):
            lastindex[char] = i #it will definetly store the last index beacuse it store the index of the very last part of the element index
        res = []
        size, end = 0,0
        for i ,char in enumerate(s):
            size += 1
            end = max(end, lastindex[char])

            if i == end:
                res.append(size)
                size = 0 # reset the size
        return res        

