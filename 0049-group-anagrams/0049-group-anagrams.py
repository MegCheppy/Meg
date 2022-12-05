class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        if len(strs) == 0:
            return []
        
        c_dict = {}
        
        for word in strs:
            freq_list = [0]*26
            
            for c in word:
                freq_list[ord(c)-ord('a')] += 1    # increment counter for freq in list
            
            freq_list = tuple(freq_list) # as tuple is immutable and can be used as key in dict
            
            if freq_list not in c_dict.keys():
                c_dict[freq_list] = [word]     # add the first word in the list
            else:
                c_dict[freq_list].append(word)  # add more anagrams to the list
                
        return c_dict.values()
