list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[:])
# 获取到 list 中所有的数据
# 输出为 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list[1:4])
# 获取到 list 中索引为 [1, 4) （前闭后开）的数据
# 输出为 [1, 2, 3]

print(list[::2])
# 从索引 0 开始，正向获取索引为 [0, len(list)) 的数据，步长为 2
# 输出为 [0, 2, 4, 6, 8]

print(list[::-2])
# 从 len(list) -1 索引开始，逆向获取索引为[len(list) - 1, 0) 的数据，步长为 2
# 输出为 [9, 7, 5, 3, 1]

print(list[8:2:-1])
# 从 索引 8 开始， 逆向获取索引为 [8,2)，步长为 1
# 输出为 [8, 7, 6, 5, 4, 3]

# 结论：
# 起始位:结束位:方向和步长位
#
# 1. 起始位默认为 0 或者 len(list) - 1（取决于方向位）闭区间。
# 2. 结束位 开区间。
