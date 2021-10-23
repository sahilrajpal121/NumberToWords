# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:10:52 2021

@author: sahil
"""

def IntegersToWords(x,intowords):
    digits=len(x)
    word=''
    exception=''
    while(x):
        if x[0]!='0':
            
            #for last 2 digit numbers that start with 1 or last digit left
            if (digits==2 and x[0]=='1') or digits==1:
                word+=f" {intowords[x]}"
                return word
            
            #for cases : fifty ,sixty nine
            elif digits%3==2:
                if digits==2:
                    word+=f"{intowords[x[0]+'0']}-{intowords[x[1]] }"
                    return word
                else:
                    temp='1'+('0'*(digits-2))
                    if x[0]=='1':
                        word+=f"{intowords[x[0:2]]} {intowords[temp]} "
                    else:    
                        word+=f"{intowords[x[0]+'0']}-{intowords[x[1]]} {intowords[temp]} "
                    x=x[2:]
                    exception=''
            
            #for cases of hundred: five hundred fifty four billion , one hundred eighty four
            elif digits%3==0 and digits>3:
                    word+=f"{intowords[x[0]]} Hundred "
                    temp='1'+('0'*(digits-3))
                    exception=intowords[temp]
                    x=x[1:]
            
            else:
                temp='1'+('0'*(digits-1))
                word+=f"{intowords[x[0]]} {intowords[temp]} "
                x=x[1:]
            digits=len(x)
        else:
            x=x[1:]
            digits-=1
            if digits and x[0]=='0':
                word+=f"{exception} " 
                exception=''
            if not x:
                return word

intowords={'0':'','1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",
           '8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen',
           '14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen',
           '20':'twenty','30':'thirty','40':'fourty','19':'nineteen',
           '50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety',
           '100':'hundred','1000':'thousand','1000000':'million','1000000000':'billion',
           '1000000000000':'trillion','1000000000000000':'quadrillion',
           '1000000000000000000':'quintillion','1000000000000000000000':'sextillion'}

import random
for key,value in intowords.items():
    if value:
        intowords[key]=value[0].upper()+value[1:]
        
#uncomment below and tweak the random number range to test it yourself!

# for i in range(100):
#     r=random.randint(0,1000000000000000000000)
#     print(r,'==',IntegersToWords(str(r), intowords),'\n')
while(1):
    x=input("Enter a number and i'll give you the english word representation or type quit to exit:\n")
    if x.lower()=='quit':
        break
    ans=IntegersToWords(x,intowords)
    print(ans)
    
