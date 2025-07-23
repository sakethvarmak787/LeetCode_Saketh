class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stk=[]
        ans=0
        if(y>x):
            for i in s:
                if(len(stk)>0):
                    if(stk[-1]=="b" and i=="a"):
                        stk.pop()
                        ans+=y
                    else:
                        stk.append(i)
                else:
                    stk.append(i)
            s="".join(stk)
            stk=[]
            for i in s:
                if(len(stk)>0):
                    if(stk[-1]=="a" and i=="b"):
                        stk.pop()
                        ans+=x
                    else:
                        stk.append(i)
                else:
                    stk.append(i)
        else:
            for i in s:
                if(len(stk)>0):
                    if(stk[-1]=="a" and i=="b"):
                        stk.pop()
                        ans+=x
                    else:
                        stk.append(i)
                else:
                    stk.append(i)
            s="".join(stk)
            stk=[]
            for i in s:
                if(len(stk)>0):
                    if(stk[-1]=="b" and i=="a"):
                        stk.pop()
                        ans+=y
                    else:
                        stk.append(i)
                else:
                    stk.append(i)
        return ans

        
        
            

        