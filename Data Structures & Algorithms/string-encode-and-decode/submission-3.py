class Solution:

    def encode(self, strs: List[str]) -> str:
        # example input -> ['pk', 'loves', 'leetcode']
        # encode will be the length followed by a #
        # this way we know how long each string is as well as where to start/stop
        res= ''
        for s in strs: 
            length= len(s)
            res += str(length) + '#' + s

        # returned result is '2#pk5#loves8#leetcode'
        return res

    def decode(self, s: str) -> List[str]:
        res= []
        i=0

        # '2#pk5#loves8#leetcode'
        while i < len(s):
            j= i
            # move j pointer to the #
            while s[j] != '#':
                j+=1
            length= int(s[i:j]) 
            i= j + 1 # move i to the first letter after the hashtag (also the first letter of the string)
            j= i + length # move j from where i is to the end of the string
            res.append(s[i:j]) # now that our pointers are in the right place, use substr to get the result and add it to the array
            i=j # reset pointers
        
        return res

