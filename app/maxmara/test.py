
s = "pwwkew"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_lis = list(s)
        num = 0
        for i in range(len(s_lis)):
            s_dic = {}
            for v in s_lis[i:]:
                if s_dic.get(v):
                    break
                s_dic[v] = 1
            if len(s_dic) > num:
                num = len(s_dic)
        return num

v1 = Solution()
v1.lengthOfLongestSubstring(s)