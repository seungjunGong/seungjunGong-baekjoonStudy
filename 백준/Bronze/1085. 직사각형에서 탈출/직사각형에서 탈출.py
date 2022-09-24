x, y, w, h = list(map(int, input().split(' ')))
distanceList = [h - y, w - x, x , y]
print(min(distanceList))