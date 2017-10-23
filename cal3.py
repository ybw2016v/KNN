#python3
import re
from cal2 import caltwo
from cal1 import welldog,calone
from sourse import sdogread
ecpdog=[('Na', '0.5'), ('O', '')]
zhongdog=['Na=23\n', 'H=1\n', 'He=4\n', 'Li=6\n', 'O=16\n','Al=27\n','C=12\n','K=39\n']
def calthree(onedog,twodog,zhongdog):
    liang=float(35)#配置35克
    print('配置'+str(liang)+'g')
    ttdog=calone(zhongdog,twodog)
    modog=float(liang/ttdog)
    ansdog={}
    two2dog=[]
    #lldog=
    for podog in twodog:
        if podog[0]=='O' or podog[0]=='C':
            pass
        else:
            two2dog.append(podog)
    lldog=caltwo(sdogread(),zhongdog)
    for itedog in two2dog:
        itedog=list(itedog)#将元组更改为列表
        ettdog=[]
        c=itedog[0]
        ettdog.append(lldog[c][2])
        if itedog[1]=='':
            itedog[1]=1
        else:
            pass
        ettdog.append(lldog[c][0]*modog*float(itedog[1]))
        ettdog.append(lldog[c][1])
        ettdog.append(lldog[c][3])
        ansdog[c]=ettdog

    return ansdog

#print(calthree(sdogread(),ecpdog,zhongdog))
