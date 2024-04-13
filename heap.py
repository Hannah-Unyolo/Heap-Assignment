import heapq
Scores = [8,1,4,5,2,7,3,6]
heapq.heapify(Scores)
print(Scores)

heapq.heappush(Scores,9)
print(Scores)

heapq.heappop(Scores)
print(Scores)