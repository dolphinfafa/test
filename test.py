import random

def coin():
    n_tosses = 10000
    coin_tosses = [random.randint(0, 1) for _ in range(n_tosses)]  # 1表示正面，0表示反面

    # 统计最多连续出现的正面次数
    max_count = 0
    count = 0
    for i in range(n_tosses):
        if coin_tosses[i] == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

# 测试1000次，每次抛10000次硬币
# 统计每次的值，并且统计这个值出现的次数,记录在字典d中
# 字典d按key的value从大到小排序，并打印
def test():
    d = {}
    for i in range(1000):
        n = coin()
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    
    # 按d[key]的值从大到小排序
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(d)

if __name__ == '__main__':
    test()