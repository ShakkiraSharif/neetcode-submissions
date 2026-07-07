class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicta={}
        for word in strs:
            i="".join(sorted(word))
            if i not in dicta:
                dicta[i]=[]
                dicta[i].append(word)
            else:
                dicta[i].append(word)
        return list(dicta.values())