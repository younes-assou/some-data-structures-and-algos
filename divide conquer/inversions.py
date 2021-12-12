def merge(x,y):
    n1 = len(x)
    n2 = len(y)
    nbr = 0

# create temp arrays
    T = [0] * (n1+n2)

# Merge the temp arrays back into arr[l..r]
    i = 0	 # Initial index of first subarray
    j = 0	 # Initial index of second subarray
    k = 0	 # Initial index of merged subarray

    while i < n1 and j < n2:
        if x[i] <= y[j]:
            T[k] = x[i]
            i += 1
        else:
            T[k] = y[j]
            j += 1
            nbr+=n1-i
        k += 1

# Copy the remaining elements of L[], if there
# are any
    while i < n1:
        T[k] = x[i]
        i += 1
        k += 1

# Copy the remaining elements of R[], if there
# are any
    while j < n2:
        T[k] = y[j]
        j += 1
        k += 1

    return (T, nbr)

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def get_number_of_inversions(arr, l, r):
    if l >= r:
        return ([arr[l]], 0)
# Sort first and second halves
    m = l+(r-l)//2
    t1, nbr1 = get_number_of_inversions(arr, l, m)
    t2, nbr2 = get_number_of_inversions(arr, m+1, r)
    t3, nbr3 = merge(t1, t2)
    return (t3, nbr1+nbr2+nbr3)


n = int(input())
a = list(map(int, input().split()))
print(get_number_of_inversions(a, 0, len(a)-1)[1])
