'''
가장 작은 2개의 묶음을 더한 뒤 해당 카드를 버리고
새로운 묶음을 추가하여 정렬한다. - 우선순위 큐 이용
위 과정을 n - 1번 반복한다.
'''
import heapq

n = int(input())

cards = []
for i in range(n):
    card = int(input())
    heapq.heappush(cards, card)

result = 0
for _ in range(n-1):
    new_card = heapq.heappop(cards) + heapq.heappop(cards)
    result += new_card
    heapq.heappush(cards, new_card)

print(result)