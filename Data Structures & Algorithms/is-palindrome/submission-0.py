class Solution:
    def isPalindrome(self, s: str) -> bool:
        m=0
        s1=""
        for i in s:
            if i.isalnum():
                s1+=i.lower()
        n=len(s1)-1
        while(m<n):
            if (s1[m]==s1[n]):
                m+=1
                n-=1
            else:
                return False
        return True
          