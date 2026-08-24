class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}
        

        for i, word in enumerate(strs):

            sorted_word = ''.join(sorted(word))
            
            if sorted_word in dict:
                dict[sorted_word].append(word)
            else:
                dict[sorted_word] = []
                dict[sorted_word].append(word)
        
        return (list(dict.values()))

            