# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:33:49 2022

@author: wjdtn
"""

'----------------------(1/1)------------------'
#ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
#kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
#aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 
#프로그램을 작성하시오.

n=int(input())
count=n

for i in range(0,n):
    context=input()
    for j in range(0,len(context)-1):
        if context[j]==context[j+1]:
            pass
        elif context[j] in context[j+1:]:
            count-=1
            break

print(count)
            