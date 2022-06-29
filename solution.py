class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        slist = list()
        
        stemp = "";
        for i in s: 
            if i not in se:
                stemp += i 
                se.add(i)
            else: 
                slist.append(stemp)
                # print(stemp[stemp.index(i)+1:])
                se.clear()
                for j in stemp[stemp.index(i)+1:]:
                    se.add(j)
                se.add(i)
                stemp = stemp[stemp.index(i)+1:] + i
                
                # print(se)
        slist.append(stemp)
        # print(slist)
        mx = 0
        
        for i in slist:
            if len(i) > mx:
                mx = len(i)
        return mx
        
