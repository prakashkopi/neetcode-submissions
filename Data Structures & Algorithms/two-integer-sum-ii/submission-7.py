class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r= 0, len(numbers)-1

        for i in range(len(numbers)): 
            summ= numbers[l] + numbers[r]
            if summ < target: 
                l +=1
            elif summ > target: 
                r-=1

        return [l+1, r+1]
            
        