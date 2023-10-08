from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        if n * k == 0:
            return []
        
        if k == 1:
            return nums
        
        def clean_deque(i):
            if deq and deq[0] == i - k:
                deq.popleft()
                
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        deq = deque()
        max_index = 0
        
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            if nums[i] > nums[max_index]:
                max_index = i
        
        result = [nums[max_index]]
        
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            result.append(nums[deq[0]])
        
        return result