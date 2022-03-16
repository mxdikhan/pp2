n = int(input())
dem, hunt = {}, {}
for i in range (n):
    d, w = input().split()
    # not w in dem 
    if dem.get(w) == None: dem[w] = 1
    else: dem[w] += 1

m = int(input())
for i in range(m):
    h, a, k = input().split()
    if dem.get(a) != None: dem[a] -= int(k)

survivors = 0
for j in dem.values():
    if j > 0: survivors += j

print ('Demons left:', survivors)