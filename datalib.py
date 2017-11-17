#!puthon3
import json
import os
from dogname import dog
print('GPL_v3')
# print(os.name)
# print(os.uname())
f=open('namelib.dat','r')
text = f.read().splitlines()
print(text)
time='2016'
context='5'
mathlen={'h':25,'n':26}
xingzhi={'dog':'cat'}
data={
	'时间':time,
	'组分':context,
	'几何尺寸':mathlen,
	'性质':xingzhi
}
# se=dog(text[0],data)
# readbookdog=se.inwrite()
# print(se.outlook())






f.close()
class pig(object):
	def __init__(self,name):
		self.dirname= name
		pass
	def list(self):
		f = open(self.dirname,'r')
		text = f.read().splitlines()
		for x in text:
			hu=dog(x,'0')
			res=hu.outlook()
			print(x,res['时间'])
			pass
		f.close()
		pass
at=pig('namelib.dat')
at.list()