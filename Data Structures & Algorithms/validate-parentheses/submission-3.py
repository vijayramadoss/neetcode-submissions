class Solution:
    def isValid(self, s: str) -> bool:
        t=[]
        l={"[":"]","{":"}","(":")"}
        for i in s:
            if(i in "({["):
                t.append(i)
            elif (i in ")}]"):
              if(len(t)>0):
                k=t.pop()
                if (l[k]==i):
                    continue
                else:
                    return False
              else:
                return False
        return len(t)==0
         
        