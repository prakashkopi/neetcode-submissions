class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams are when 2 strings have exact same characters (& therefore length)
        # create a hashmap str : freq array with 26 characters
        # ex- hac : [1,0,1,0,0,0,0,1,0,0 etc]
        # because    a   c         h
        
        res= defaultdict(list)

        for s in strs: 
            count= [0] * 26 #initialize freq array
            for c in s: 
                count[ord(c) - ord('a')] += 1
            # basically now every string that has the same characters will be added to the values list in the dictionary
            # because they will have the same key (which is the freq array) so the .append(s) will append that string
            # to the existing key which is the tuple(count)
            # final hashmap 
            # {
            # (1,0,0,0,1,0,...,1): ["eat", "tea", "ate"],
            # (1,0,0,0,0,0,...,1): ["tan", "nat"],
            # (1,1,0,0,0,0,...,1): ["bat"]
            # }
            res[tuple(count)].append(s) # convert to tuple bc list are mutable and cant be used as a dictionary key 

        return list(res.values())
        