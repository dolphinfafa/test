import random

# 随机抛n次硬币，统计最多连续出现的正面次数
def coin(n):
    max_count = 0
    count = 0
    for i in range(n):
        if random.randint(0, 1) == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

# 测试1000次，每次抛1000次硬币
# 统计每次的值，并且统计这个值出现的次数
# 输出最多连续出现的正面次数及其出现次数
def test():
    d = {}
    for i in range(1000):
        n = coin(1000)
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    max_count = max(d.keys())
    
    # 按d[key]的值从大到小排序
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print("最多连续出现的正面次数及其出现次数：")
    print("max_count: ", max_count)
    print("count: ", d[0][1])

if __name__ == '__main__':
    test()