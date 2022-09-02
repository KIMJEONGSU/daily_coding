# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:07:57 2022

@author: wjdtn
"""

'------------------------------(2/4)------------------------------'

#문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
#즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
#S에는 QR Code "alphanumeric" 문자만 들어있다.

#QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

#코드 1
a= int(input())

for i in range(a):
    a,b=list(map(str,input().split()))
    for z in b:
        print((z*int(a)).upper(),end='')



#코드 2
a= int(input())

for i in range(a):
    a,b=list(map(str,input().split()))
    result=''
    for z in b:
        result+=z*int(a)
    print(result.upper())
        
    
    
'------------------------------(2/2)------------------------------'
#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 
#무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

#코드1
context = input().upper()

dic_set = list(set(context))   #set으로 중복값 제거
dic_list = []    

for i in dic_set:         
    count = context.count(i)  #입력받은 문자에서 dic_set와 같은 문자가 있으면 
                              #count해서 dic_list에 저장
    dic_list.append(count)
    
if dic_list.count (max(dic_list)) > 1:     #dic_list에서 값은 값이 1개 초과하면 ?출력
    print('?')
else :
    max_i = dic_list.index (max(dic_list))
    print(dic_set [max_i] )





