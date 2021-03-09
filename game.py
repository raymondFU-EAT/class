class Player: # 創造了一個遊戲
	def __init__(self, name, ad, df): # 設定了四個屬性(class本身,姓名,攻擊,防禦)
		print('我誕生了')
		self.name = name # 自身的name是name(後來可以取名)
		self.blood = 100
		self.ad = ad
		self.df = df

	def protect_player(self, target): # 定義攻擊的模式
		target.blood = target.blood-( self.ad - target.df ) # 被攻擊的目標剩餘的血量
		
	def mix(self, target1, target2):
		self.blood = self.blood - (target1.ad + target2.ad -self.df) # 本身被攻擊後剩下的血量
		# 本身血量 = 本身血量 - (來自目標1的攻擊 + 來自目標2的攻擊 - 本身的防禦)
	def back(self, target): # target 反擊了 self 的傷害,反而對self造成了傷害,導致self血量下降
		self.blood = self.blood - abs((self.ad - target.ad + self.df)) # 被攻擊後反擊目標,目標剩下的血量
		# 本身血量 = 本身血量 - 絕對值(本身的攻擊 - 反擊者給我的攻擊 + 本身防禦)

p1 = Player('player1', 20, 5)
p2 = Player('player2', 30, 5)
p3 = Player('player3', 40, 5)
p = [p1, p2, p3] # 設定的class可以直接當列表
for s in p:      # 直接可以用for迴圈把一列列要的資料叫出來
	print(s.name, '血量', s.blood, '攻擊力',  s.ad, '防禦力',  s.df)
p3.protect_player(p1)
print('玩家', p1.name, '防禦了', p3.name,'的攻擊,血量剩下', p1.blood)
p3.mix(p1, p2)
print('玩家', p3.name, '受到玩家', p1.name, '和,玩家', p2.name, '合擊後,生命剩下',
     p3.blood )
p1.back(p3)
print('玩家', p3.name, '反擊了來自', p1.name, '的傷害,導致於,玩家', p1.name, '血量剩下',
     p1.blood )


#print('玩家', p1.name, '受到玩家', p2.name, '的攻擊', '血量剩下', p2.blood)
