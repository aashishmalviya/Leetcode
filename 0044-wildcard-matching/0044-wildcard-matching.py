# Linear time (len(s)+len(p))


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, slen = 0, len(s)
        j, plen = 0, len(p)
        last_pstar_location = -1
        s_btrk = -1

        while (i < slen):
            if j < plen and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
                continue

            if j < plen and p[j] == '*':
                last_pstar_location = j
                s_btrk = i
                j += 1
                continue

            # atleast 1 unused * has been found
            # we match the last found * to current mismatch char in s and
            # we start both the string and pattern from their next indexes
            # from where the last * was found 
            if last_pstar_location != -1:
                j = last_pstar_location + 1
                s_btrk += 1
                i = s_btrk
                continue

            # Mismatch and no * found yet
            return False
        return all([p_char == "*" for p_char in p[j:]])

#         while j < plen:
#             if p[j] != '*':
#                 return False
#             j += 1

#         return True


# Bottom Up
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
        
#         def solverTab(s: str, p: str) -> bool:
#             #dp = [[False for j in range (len(p)+1)] for _ in range(len(s) + 1)]
            
#             prev = [False for j in range(len(p) + 1)]
#             curr = [False for j in range(len(p) + 1)]

#             prev[0] = True
                
#             for j in range(1, len(p)+1):
#                 if(p[j-1] == '*' ):
#                     prev[j] = prev[j-1];

#             for i in range(1, len(s) + 1):
#                 for j in range(1, len(p) + 1):

#                     if s[i-1] == p[j-1] or p[j-1] == '?':
#                         curr[j] = prev[j-1]
 
#                     elif p[j-1] == '*':
#                         curr[j] = curr[j-1] or prev[j]
#                     else:
#                         curr[j] = False
            
#                 prev = curr[:]

#             #print(dp)
#             return prev[len(p)]





# Top Down
#         dp = [[-1] * (len(p)+1) for _ in range(len(s) + 1)]
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

#        return solverTab(s, p)