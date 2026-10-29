class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        def compare_chars(s_indx, t_indx):
            if s_indx == s_len:
                return True
            elif t_indx == t_len:
                return False
            if s[s_indx] == t[t_indx]:
                s_indx += 1
            t_indx += 1
            return compare_chars(s_indx, t_indx)

        return compare_chars(0, 0)
