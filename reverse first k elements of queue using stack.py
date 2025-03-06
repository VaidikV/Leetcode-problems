from collections import deque

def reverse_first_k_elements(k, q):
    stack = []
    for i in range(k):
        stack.append(q.popleft())

    while stack:
        q.append(stack.pop())

    for i in range(len(q) - k):
        q.append(q.popleft())

    return q

q = deque([1,2,3,4,5,6,7,8,9])
k = 5

print(reverse_first_k_elements(k, q))