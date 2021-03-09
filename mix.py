from data.db import Db # 把data資料夾中的db.py讀取出class Db

class Mix:
	def __init__(self):
		print('asdasdasd')
		self.db = Db() # 把Db這個class給實體化,做成一個物件存起來
		

z = Mix() 
