from collections import deque
q=deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q
q.append(5)
q


import heapq
num=[1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,num))
print(heapq.nsmallest(3,num))



portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap=heapq.nsmallest(3,portfolio,key=lambda x:x['price'])
cheap
