# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:56:32 2022

@author: wjdtn
"""

#이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.



#처음에 쓴 코드지만, 잘못된 결과 출력.
# 규칙은 찾았지만 코드로 구현해내지 못함.

N=int(input())
result=[]


for i in range(1,N):
    result.append(str(i)+'/'+str(i))
    
    for j in range(2,N):
        result.append(str(1)+'/'+str(j))

        for z in range(j,1,-1):
            result.append(str(z)+'/'+str(z-1))
        
a=list(dict.fromkeys(result))
print(a)


'-----------------------------------'
#분수를 나눠서 생각해보자
#메모리 초과, 문제 잘못 이해함.
N=int(input())
a=[]
b=[]
line=1

for i in range(1,N+1):
    for j in range(1,i+1):
        a.append(j)
        
for x in range(1,N+1):
    for y in range(x,0,-1):
        b.append(y)    
    

print(a[N-1],'/',b[N-1],sep='')

'-----------------------------------'
#다른 사람의 코드

n = int(input())
line = 1

while n > line :
    n -= line
    line += 1

if line % 2 == 0 :
    num1 = n
    num2 = line - n + 1
elif line % 2 == 1 :
    num1 = line - n + 1
    num2 = n


print(num1,'/',num2,sep = "")





