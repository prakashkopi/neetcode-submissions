class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort algorithm
        # Input: nums = [1,2,2,3,3,3,3], k = 2


        count= {}
        freq= [[] for i in range(len(nums) + 1)]        

        # map num : count
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        # go through the count map, place the num in the index of the count
        # example, 3 appears 4 times above, so the 4th index of the array
        # would have 3
        for num, cnt in count.items():
            freq[cnt].append(num)

        # loop backwards through the freq array
        # add each number to the res array, once res == k length, return
        # since freq is an array within an array, even if there's 2 numbers 
        # with same freq [2,3], res.append will get both of them 
        res= []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]: # freq[i] because freq is an array with array inside
                res.append(num)
            if len(res) == k: 
                return res
    


        