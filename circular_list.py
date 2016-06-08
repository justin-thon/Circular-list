from collections import deque

#demo
#Test edit online

def circular_list(l):
    l=deque(l)
    l.append(l.popleft())
    return l
