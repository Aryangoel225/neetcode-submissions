class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # my_dict = defaultdict(list)  key [cat] = "str value"
        my_dict = defaultdict(list)
        # loop through str array
        for s in strs:
            charList = tuple(sorted(s))
            my_dict[charList].append(s)
        return [valuelist for valuelist in my_dict.values()]
        ## charList = tuple(sorted(s))
        # append value (takes care of the new key issue) 
        # return [for value in hashmap.values()]