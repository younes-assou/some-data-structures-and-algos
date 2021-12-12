# python3

from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    stack = deque()

    for i in range(m):
        while stack and sequence[i] >= sequence[stack[-1]]:
            stack.pop()

        stack.append(i)

    for i in range(m,len(sequence)):
        maximums.append(sequence[stack[0]])

        while stack and stack[0] <= i-m:
            stack.popleft()

        while stack and sequence[i] >= sequence[stack[-1]]:
            stack.pop()

        stack.append(i)
    maximums.append(sequence[stack[0]])

    return maximums

n = int(input())
input_sequence = [int(i) for i in input().split()]
assert len(input_sequence) == n
window_size = int(input())

print(*max_sliding_window_naive(input_sequence, window_size))

