class Solution:
    def isPalindrome(self, s: str) -> bool:
        sta = 0
        end = len(s) -1
        
        while sta < end:
            # print(s[sta], s[end])
            while s[sta].isalnum() == False:
                sta += 1
                if sta > end:
                    return True

            while s[end].isalnum() == False:
                end -= 1
                if sta > end:
                    return True

            if s[sta].isdigit() or s[end].isdigit():
                if s[sta] == s[end]:
                    sta += 1
                    end -= 1
                else:
                    return False
            else:
                if s[sta].lower() == s[end].lower():
                    sta += 1
                    end -= 1
                else:
                    return False
            
        return True