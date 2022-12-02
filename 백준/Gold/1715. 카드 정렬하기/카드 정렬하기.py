import heapq
deckList = []
sum_deck = 0
N = int(input())

for _ in range(N):
    heapq.heappush(deckList, int(input())) 
 
for _ in range(N-1):
    new_deck = heapq.heappop(deckList) + heapq.heappop(deckList)
    sum_deck += new_deck
    heapq.heappush(deckList, new_deck)

print(sum_deck)