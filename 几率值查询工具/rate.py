#!/usr/bin/env python3
while True:
    i=0
    dict={}
    with open('data.txt','r') as f:
        for line in f.readlines():
            if i<98.0:
                index=round(i,1)
                dict[index]=line.replace('\n','')
                i+=0.1
            else:
                j=i-0.09
                index=round(j,2)
                dict[index]=line.replace('\n','')
                i+=0.01
    rate=float(input('请输入抑制率：'))
    print(dict[rate])

