# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:51:21 2022

@author: wjdtn
"""



#땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
#달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
#달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

'''
a,b,v=map(int,input().split())

cnt=0
suum=0

for i in range(v):
    suum+=a
    if suum>=v:
        cnt+=1
        break
    else:   
        suum-=b
        cnt+=1
    
print(cnt)
'''
#위의 코드는 정답은 잘나왔지만 몇개는 시간초과

#다른 사람의 코드
#k식에 대한 이해는 됐지만, /대신 //는 왜 안될까?

a,b,v = map(int,input().split())

k = (v-b)/(a-b)

print(int(k) if k == int(k) else int(k)+1)


























