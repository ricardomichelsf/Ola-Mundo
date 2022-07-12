a, b = input().split(" ")
a = int(a)
b = int(b)
nomes = []

for i in range(a):
    y = input()
    nomes.append(y)

alfabetica = sorted(nomes)

print(alfabetica[b - 1])