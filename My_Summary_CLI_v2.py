class Summary:
	def __init__(self, choice):
		self.choice = choice
	def openSum(self):
		f = open(self.choice)
		while True:
			line = f.readline()
			if len(line) == 0:
				break
			print(line, end = ' ')
		
try:	
	print ('Choose the language of the Summary: 1 - English, 2 - Russian')
	while True:
		x = (input('\nEnter your choice:'))
		if (x == '1'):
			Summary('My_Summary_Eng.txt').openSum()
		elif (x == '2'):
			Summary('My_Summary_Rus.txt').openSum()
		else:
			print('\nYour choice is wrong...\nTry again!')
except KeyboardInterrupt:
	print('\n')
	
