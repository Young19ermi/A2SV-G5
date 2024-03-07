class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letter = list(string.ascii_lowercase)
        numbers = [i for i in range(1,27)]
        k = dict(zip(letter,numbers))
        print(k)
       
        i = 0 
        j = len(letters)-1

        if k[letters[i]] > k[target] or k[letters[j]] <= k[target]:
            return letters[i] 

       
        while i <= j:
            mid = (i+j)//2

            if letters[mid] == target:
                i = mid+1

            elif k[target] < k[letters[mid]]:
                j = mid-1
            else:
                i = mid+1
        return letters[i]

