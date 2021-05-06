# Task # 1

# 1 Method
l = [1, 2, 3]
l1 = [i * 2 for i in l]
print(l1)

# 2 Method
l2 = []
for i in range(3):
    l2.append(l[i] * 2)
print(l2)


# Task # 2

l3 = [1, 2, 3]
res = 0
for num in l3:
    res += num ** 2
print(res)


# Task # 3

# 1 Method
timeM_1_1 = 3 * 0.5
timeM_1_2 = 6.7 * 0.5
timeM_1_3 = 11.8 * 0.5
print(int(timeM_1_1), int(timeM_1_2), int(timeM_1_3))

# 2 Method
timeM_2_1 = 3
timeM_2_2 = 6.7
timeM_2_3 = 11.8
print(int(timeM_2_1 / 2), int(timeM_2_2 / 2), int(timeM_2_3 / 2))

# 3 Method
timeM_3_1 = 3
timeM_3_2 = 6.7
timeM_3_3 = 11.8
print(int(timeM_3_1 / 2), int(timeM_3_2 / 2), int(timeM_3_3 / 2))


# Task # 4

s = 'Hello world'
if ' ' in s:
    print(s.upper())
else:
    print(s.lower())
