class Solution:
    def countPrimes(self, n: int) -> int:
        if n==2:
            return 0
        l=[1]*n
        for i in range(2,int(sqrt(n))+1):
            if l[i]==1:
                for j in range(i*i,n,i):
                    l[j]=0
        c=0
        for i in range(2,n):
            if l[i]==1:
                c+=1
        return c
