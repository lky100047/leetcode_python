class Solution:
    def makeGood(self, s: str) -> str:
        i = 0;
        while(i < len(s)):
            temp = i;
            i = i + 1;
            if(temp+1<len(s)):
                if(abs(ord(s[temp])-ord(s[temp+1]))==32):
                    s = s.replace((s[temp] + s[temp+1]), "", 1);
                    i = 0;
        return s;
