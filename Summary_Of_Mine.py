#import PyPDF2
try:	
	print ('Choose the language of the Summary: 1- English, 2 - Russian')
	while True:
		x = (input('\nEnter your choice:'))
		if (x == '1'):
			f = open('My_Summary_Eng.txt')
			while True:
				line = f.readline()
				if len(line) == 0:
					break
				print(line, end = ' ')
		elif (x == '2'):
			f = open('My_Summary_Rus.txt')
			while True:
				line = f.readline()
				if len(line) == 0:
					break
				print(line, end = ' ')
		else:
			print('\nYour choice is wrong...\nTry again!')
except KeyboardInterrupt:
	print('\n')
	
