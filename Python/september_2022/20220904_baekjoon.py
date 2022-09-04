# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 23:22:03 2022

@author: wjdtn
"""

'------------------------------(1/2)------------------------------'
#예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 
#이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 
#이루어져 있는지 출력한다.

#코드1
'''
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

n=input()
result=n

count=0

for i in range(len(croatia)):
    if croatia[i] in result:
        count+=1
        result=result.replace(croatia[i],'')
        
       
print(count+(len(result)))
'''
#문제점
#nljj을 입력했을때 3이 나와야하는데, 위의 코드로 실행시 2 출력
#lj인식 후 삭제하면 result는 nj가 된다. nj가 croatia에 있어서 총 2로 출력

#코드2
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

n=input()

for i in range(len(croatia)):
    n=n.replace(croatia[i],'!')
        
print(len(n))

#croatia에 포함된 문자가 있으면 !로 바꾸고 최종 문자 길이를 출력한다.
 
        
        
        











'------------------------------(2/2)------------------------------'