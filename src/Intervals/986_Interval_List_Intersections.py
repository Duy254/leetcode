def intervalIntersection(A, B):
    res = []
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])

        if lo <= hi:
            res.append([lo,hi])
        
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return res

# Complexity: O(n+m) 
# Space: O(m+n) to store