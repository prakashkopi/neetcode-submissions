class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap --> num : count
        count = {}
        for n in nums:
            count[n]= 1 + count.get(n, 0)

        arr= []
        for n, c in count.items():
            arr.append([c, n])
        arr.sort()

        res= []
        while len(res) < k: 
            # since array is sorted, pop will take off the largest element and append it to res array
            # [1] gets the num values because it's stored [cnt, num]
            res.append(arr.pop()[1])

        return res
        