#https://edabit.com/challenge/MfypAQedEAun4oQFA

def perrin(n):
    lst = [3,0,2]
    for i in range(3,n+1):
        lst.append(lst[i-3] + lst[i-2])
    return lst[n]


###
def perrin(n):
    a=[3,0,2]
    if n<2:
        return a[n]
    else:
        for i in range(n-2):
            a.append(a[i]+a[i+1])
    return a[-1]

    #
def perrin(n):
	A, i=[3,0,2], 3
	while len(A)<=n:
		A.append(A[i-3]+A[i-2])
		i+=1
	return A[0]*(n==0)+A[1]*(n==1)+A[2]*(n==2)+A[-1]*(n>=3