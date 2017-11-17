#!python3
#管理数据文件，面向对象？
import os
import json 
class dog(object):
	# name='/0'
	# data='/0'

	def __init__(self,name,data):
		self.name = name
		self.data = data

	def inwrite(self):
		f = open(self.name,'w')
		#print(self.name)
		jsdog = json.dumps(self.data)
		f.write(jsdog)
		f.close()
		pass
	def outlook(self):
		f = open(self.name,'r')
		textdog = f.read()
		return json.loads(textdog)
		f.close()
		pass

# lu=dog('001.knn','223')
# lu.inwrite()
# print(lu.outlook())
