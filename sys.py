#python3
import re
from prettytable import PrettyTable
#import indog
from indog import shi
from cal1 import welldog,calone
from sourse import sdogread
from cal3 import calthree
from post import knnpost
zhiliang={}
listdata=[]
aimdog={}
def start():
    '''启动界面'''
    print("KNN PROGECT")
    print('<GPLv3>')
start()
conf=''
def readconf():
    global conf
    conf=['','']
    '''读取配置文件'''
    f = open ('data.conf','r')

    #conf=0
    #while True:

    fline = f.readlines()
    ###删除注释
    for i in fline:
        if i.startswith('#') or not re.match('.*=.*',fline[fline.index(i)]):
            del fline[fline.index(i)]
        else:
            pass


    conf=fline


    #print(conf)
    f.close()
    return conf
def hconf(confl):
    '''对配置文件中的信息进行解读'''
    #print(confl)
    comdog=re.compile(r'(.*)=(.*)')
    for j in confl:
        jdog=comdog.findall(j)
        zhiliang[jdog[0][0]]=float(jdog[0][1])
    #print(zhiliang)
    print('正在导入信息……')
    for name , mass in zhiliang.items():
        print("元素： "+name.ljust(3)+'相对原子质量：'+str(mass))

def indog():
    aimdog=input('目标产物：')
    return aimdog

hconf(readconf())
#print(zhiliang)
#hconf(ll)
#readconf()
#hconf(readconf())
#print(conf)
#print(shi(indog()))
dogin=indog()
shidog=shi(dogin)#warn
# print(shidog)
# print(conf)
# print(calone(conf,shidog))
ans=calthree(sdogread(),shidog,conf)

table = PrettyTable(["元素", "来源","纯度","质量(g)"])
for ansdog in ans:
    table.add_row([ansdog,ans[ansdog][0],ans[ansdog][3],("%.4f" % ans[ansdog][1])])
anslines=dogin+'\n'+str(table)
print(anslines)
keydog=input("send the results to KNN?(y/n)")
if keydog=='y':
    knnpost(anslines)
else:
    pass


