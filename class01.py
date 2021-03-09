class Student: # 設立一個新的class項目名為Student(因為提到的屬性重複性太多才需要寫class),class可以先裝著自身的屬性
	def __init__(self, name, score): # 定義該被格式化的class 中有三樣屬性(本身,姓名,分數)
		self.name = name # 自身的名子是姓名
		self.score = score
		print('我出生了')
	def play(self):
		print(self.name, '先玩一下')
		self.score -= 20
	def do_hwk(self):
		print(self.name, '該讀書了')
		self.score += 40

s1 = Student('Ray', 60) # 因為class第一個投幣區為self所以只須丟入兩枚硬幣(name, score)
s2 = Student('Ke', 100)
print('同學: ', s1.name, '成績原來分數: ', s1.score)
s1.play()
print('同學: ', s1.name, '因為愛玩', s1.score)
print('同學: ', s2.name, '成績原來分數: ', s2.score)
s2.do_hwk()
print('同學: ', s2.name, '因為有讀書', s2.score)

students = [s1, s2]
for s in students:
	print(s.name)
