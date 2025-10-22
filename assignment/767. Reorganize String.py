class Solution(object):
    def reorganizeString(self, s):
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        

        max_freq = 0
        max_char_index = 0
        for i in range(26):
            if freq[i] > max_freq:
                max_freq = freq[i]
                max_char_index = i
        

        if max_freq > (len(s) + 1) // 2:
            return ""

        res = [''] * len(s)
        idx = 0

        while freq[max_char_index] > 0:
            res[idx] = chr(ord('a') + max_char_index)
            idx += 2
            freq[max_char_index] -= 1

        for i in range(26):
            while freq[i] > 0:
                if idx >= len(s):
                    idx = 1  
                res[idx] = chr(ord('a') + i)
                idx += 2
                freq[i] -= 1

        return ''.join(res)



solution = Solution()
print(solution.reorganizeString("aab"))    
print(solution.reorganizeString("aaab"))  