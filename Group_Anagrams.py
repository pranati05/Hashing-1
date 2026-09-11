class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        if not strs:
            return strs
        dict = {}
        arr = []
        output = []
        for i in strs:
            key = ''.join(sorted(i))
            if i not in dict:
                dict[i] = arr
            else:
                dict[i] = arr.append(i)

        for i in dict:
            output.append(dict[i])

        return output
    
#Time - O(NKlogk) k is each word so sorting k words is klogk and N is the number of words in array.
#Space - O(Nk)