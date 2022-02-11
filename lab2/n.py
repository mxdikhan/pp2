players = []

while True:
    n = int(input())
    if n == 0:
        break
    players.append(n)

res = []

while len(players) > 0:
    x = players[0] + players[-1]
    res.append(x)
    players.pop(0)
    players.pop(-1)
    if len(players) == 1:
        res.append(players[0])
        players.pop(0)
        break

for i in res:
    print(i, end = ' ')