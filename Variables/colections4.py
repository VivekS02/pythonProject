from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)

d.popleft()
d.clear()
d.extend([4,5,6])
d.extendleft([4,5,6])

d.rotate(-1)

print(d)