# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 17:10:31 2022

@author: wjdtn
"""
'------------------------(1/4)---------------------------'
#등차수열이란?
#연속하는 두 항의 차이가 모두 일정한 수열
#ex) 1,3,5,7,9....은 등차수열이다.

#공차란?
#두 항의 차이가 이 수열의 모든 연속하는 두 항들에 대해서 공통된 차이므로, 
#공차라고 한다. 여기서 공차는 2이다.

#한수란?
#정수 X의 각 자리가 등차수열을 이루면 한수라고 한다.
#한자리 수는 따로 비교할 수들이 없어서 한수로 인정한다.
#두자리 수는 구할 수 있는 공차가 1개밖에 없기 때문에 한수로 인정한다.

n=int(input())  #숫자입력
hansu=0

for i in range(1,n+1):
    if i >=100:      #세자리수라면
       i=list(map(int,str(i)))   #숫자를 숫자->정수로 리스트생성
       if i[0]-i[1]==i[1]-i[2]:   #연속된 숫자들의 차이구해서
           hansu += 1           #차이가 같으면 한수+1
     
    else: 
       hansu += 1  #한자리, 두자리는 모두 한수로 인정하기
        
print(hansu)

'------------------------(2/4)---------------------------'

#아스키코드란?
#영문 알파벳을 사용하는 대표적인 문자 인코딩
#chr() : 문자->아스키코드
#ord(): 아스키코드->문자


n=input()
print(ord(n))

'------------------------(3/4)---------------------------'

#입력받은 숫자의 자릿수 모두 더하기
#문자열에서 정수로 변환해서 하나씩 더함.

N=int(input()) #입력받은 숫자자리수
M=input()  #숫자입력
result=0

for i in M:
    result+=int(i)
    
print(result)

'------------------------(4/4)---------------------------'
#알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 
#단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
#포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

#처음 작성한 코드

from string import ascii_lowercase   #A~Z 리스트 가져오기
alphabet_list = list(ascii_lowercase)
n=list(input().lower())   #문자입력받음과 동시에 소문자로 변환


for i in n:
    for j in range(len(alphabet_list)):
        if i in alphabet_list:
           alphabet_list[j]=n.index(i)
        else:
           alphabet_list[j]=-1
               
        
for i in alphabet_list:
    print(i,end=' ')
    
    
    
#다른 사람의 코드를 참고해서 작성한 코드
from string import ascii_lowercase   #A~Z 리스트 가져오기
alphabet_list = list(ascii_lowercase)
n=list(input().lower())   #문자입력받음과 동시에 소문자로 변환


for i in alphabet_list:
    if i in n:
        print(n.index(i),end=' ')
    else:
        print(-1,end=' ')
               
        



