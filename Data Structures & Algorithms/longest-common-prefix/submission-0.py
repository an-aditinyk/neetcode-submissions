class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            for i in range(len(min(strs, key=len))):

                for j in range(len(strs)):

                    if strs[j][i] != strs[0][i]:
                        return strs[0][:i]

            return strs[0][:len(min(strs, key=len))]