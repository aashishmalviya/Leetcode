class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        #dp = [[-1] * (len(p)+1) for _ in range(len(s) + 1)]

        def solverTab(s: str, p: str) -> bool:
            dp = [[False for j in range (len(p)+1)] for _ in range(len(s) + 1)]
            
            dp[0][0] = True

            # for j in range(1, len(p)+1):
            #     flag = True
            #     for k in range(1, j+1):
            #         if p[k-1] != '*':
            #             flag = False
            #             break
            #     dp[0][j] = flag
                
            for j in range(1, len(p)+1):
                if(p[j-1] == '*' ):
                    dp[0][j] = dp[0][j-1];
                
            # for j in range(1,m+1):
            # if(p[j-1] == '*' ): dp[0][j] = dp[0][j-1];

            for i in range(1, len(s) + 1):
                for j in range(1, len(p) + 1):

                    if s[i-1] == p[j-1] or p[j-1] == '?':
                        dp[i][j] = dp[i-1][j-1]
 
                    elif p[j-1] == '*':
                        dp[i][j] = dp[i][j-1] or dp[i-1][j]


            #print(dp)
            return dp[len(s)][len(p)]



#         def solver(i, j) -> bool:
#             if i==0 and j==0: return True

#             if i>0 and j==0: return False

#             if i==0 and j>0:
#                 for k in range(1, j+1):
#                     if p[k-1] != '*':
#                         return False
#                 return True

#             if dp[i][j] != -1:
#                 return dp[i][j]

#             if s[i-1] == p[j-1] or p[j-1] == '?':
#                 dp[i][j] = solver(i-1, j-1)
#                 return dp[i][j]

#             elif p[j-1] == '*':
#                 dp[i][j] = solver(i, j-1) or solver(i-1, j)
#                 return dp[i][j]

#             else:
#                 return False

        return solverTab(s, p)