# -*- coding: utf-8 -*-
# @Time   : 2021/8/27 18:46
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : test.py.py

import sys
class Solution():
    def Find_mid(self, m, n, o, listA = [], listB = [], listC = []):
        total_list = []
        # for i in listA
        total_list = listA + listB + listC
        total_list.sort()
        if not len(total_list) % 2 ==0:
            idx = int(len(total_list) / 2 - 1)
            return total_list[idx]
        else:
            mid_1, mid_2 =  int(len(total_list) / 2 - 1), int(len(total_list) / 2)
            return (total_list[mid_1] + total_list[mid_2]) / 2

# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    total_list = []
    a = sys.stdin.readline().strip(',')
    m, n, o = int(a[0]), int(a[2]), int(a[4])
    for j in range(3):
        array = sys.stdin.readline().strip(',')
        array = list(map(int, array.split(',')))
        for num in array:
            total_list.append(num)
    total_list.sort()
    if not len(total_list) % 2 == 0:
        idx = int(len(total_list) / 2 - 1)
        print(total_list[idx])
    else:
        mid_1, mid_2 = int(len(total_list) / 2 - 1), int(len(total_list) / 2)
        print((total_list[mid_1] + total_list[mid_2]) / 2)
