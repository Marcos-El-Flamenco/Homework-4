def median(A,B):

    if len(A) > len(B):
        C = A
        A = B
        B = C
    ##Maintenant A est le plus petit des deux
    n = len(A)
    m = len(B)

    if A[n-1] <= B[0]:
        if (n+m)%2 == 1:
            return float(B[(n+m)//2 - n])
        else:
            if n == m: return (A[n-1] + B[0])/2
            else: return (B[(n+m)//2 - n - 1] + B[(n+m)//2 - n ])/2

    if B[m-1] <= A[0]:
        if (n+m)%2 == 1:
            return float(B[(n+m)//2])
        else:
            if n == m: return (B[m-1] + A[0])/2
            else: return (B[(n+m)//2] + B[(n+m)//2 + 1])/2


    i = (n-1)//2
    a = 0
    b = n-1
    done = False
    while not done:
        j = (n+m)//2  - 2 - i
        if A[i] > B[j+1]:
            b = i-1
            i = (b-a)//2
        elif A[i+1] < B[j]:
            a = i + 1
            i = (b-a)//2
        else:
            done = True
    if (n+m)%2 == 0:
        return (max(A[i],B[j]) + min(A[i+1],B[j+1]))/2
    else:
        return max(A[i+1],B[j])
