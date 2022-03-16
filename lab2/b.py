a = int(input())
b = [] 
for i in input().split():
    b.append(int(i))

b.sort()
b.reverse()
v = b[0] * b[1]

print(v)

# name_of_list[index_of_element]

