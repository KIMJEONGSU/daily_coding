# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 14:14:24 2022

@author: wjdtn
"""

'-------------------------(1/3)------------------------'
#영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 
#이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 
#단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

'''
n=map(str,input().split())

count=0
for i in n:
    count+=1
    
print(count)

'''
'-------------------------(2/3)------------------------'
#상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 
#예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 
#따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
#두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
'''
n=map(int,input().split())

m=[]
for i in n:
    m.append(int(str(i)[::-1]))
    
m.sort()
print(m[-1])
    

'''
'-------------------------(3/3)------------------------'
#숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 
#한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
#상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 
#즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
#할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.


number=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']


n=input().upper()
time=0

for i in range(len(n)):
    for j in number:
        if n[i] in j:
            time+=number.index(j)+3
            
print(time)
    










