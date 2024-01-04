class Solution:
    def minProcessingTime(self, time: List[int], task: List[int]) -> int:
        #The larger task should be given to the processor which is ready at earliest.
        time.sort()
        task.sort(reverse = True)
        the_max = 0
        for i in range(len(time)):
            the_max = max(the_max, time[i] + max(task[i*4:i*4+4]))
        return the_max





        