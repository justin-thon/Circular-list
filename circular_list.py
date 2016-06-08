from collections import deque

#demo

def circular_list(l):
    l=deque(l)
    l.append(l.popleft())
    return l
