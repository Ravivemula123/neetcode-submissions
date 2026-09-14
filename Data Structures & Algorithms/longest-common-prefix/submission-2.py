class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""
        m = len(strs[0])
        n = len(strs)

        for i in range(m):
            for j in range(1,n):

                if i +1 > len(strs[j]) or strs[0][i] != strs[j][i]:
                    return ans

            ans += strs[0][i]

        return ans 
        