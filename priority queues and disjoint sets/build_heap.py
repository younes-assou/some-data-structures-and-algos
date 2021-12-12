# python3

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    size = len(data)
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

    def sift_down(i):
        minindex = i
        l = 2*i+1
        if l<size and data[l]<data[minindex]:
            minindex = l

        r = 2*i+2
        if r<size and data[r]<data[minindex]:
            minindex = r

        if i != minindex:
            data[i], data[minindex] = data[minindex], data[i]
            swaps.append((i,minindex))
            sift_down(minindex)
        
    for i in reversed(range(0,size//2)):
        sift_down(i)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
if __name__ == "__main__":
    main()
