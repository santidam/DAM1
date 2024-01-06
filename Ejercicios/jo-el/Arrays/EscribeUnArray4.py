k = int(input())
n = input()
n1 = n.split(" ")
num = int(input())
for i in range(k):
    n1[i] = int(n1[i]) + num
for j in n1:
    print(j, end=" ")

