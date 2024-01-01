a = int(input())
x = 0
for i in range(1, a + 1):
    a = int(input())
    print((a * (a + 1) * (2 * a + 1)) // 6)
    # for y in range(1, a + 1):
    #     x += y * y
    #     print(x)
