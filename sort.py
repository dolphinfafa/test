# 随机生成一个字典，key的值是a到g，value是0-100之间的随机数字，然后按value从大到小排序
import random

def random_dict():
    d = {}
    for i in range(10):
        d[chr(random.randint(97, 103))] = random.randint(0, 100)
    return d

def sort_dict(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    d = random_dict()
    print("原字典：", d)
    print("排序后：", sort_dict(d))