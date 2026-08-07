class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(0,numRows):
            temp=[]
            for j in range(0,i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j-1]+res[i-1][j])
            res.append(temp)
        return res