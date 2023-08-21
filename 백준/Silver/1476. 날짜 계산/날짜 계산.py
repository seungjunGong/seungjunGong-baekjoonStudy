E, S, M = map(int, input().split())

year, Ei, Si, Mi = 1, 1, 1, 1

while(Ei != E or Si != S or Mi != M):
    Ei = Ei % 15 + 1
    Si = Si % 28 + 1
    Mi = Mi % 19 + 1
    year += 1

print(year)