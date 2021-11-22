# -*- coding: utf-8 -*-
# @Time   : 2021/8/27 20:09
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : sample.py.py
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    print(type(sys.stdin.readline().strip()))
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        print(line)
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)