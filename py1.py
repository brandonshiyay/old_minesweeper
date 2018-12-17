import random

class mineSweeper:
	status = False
	TrueSight = []
	for i in range(10):
		TrueSight.append([])
		for j in range(10):
			TrueSight[i].append(' ')

	minesList = []
	flags = []

	empty = []
	for i in range(10):
		empty.append([])
		for j in range(10):
			empty[i].append('/')

	def layout(list):
		print('  -----------------------------------------')
		for i in range(len(list)):
			if len(list) - i >= 10:
				line = str(len(list)-(i)) + '| '
			elif len(list) - i<10:
				line = str(len(list) -(i))+' | '
			for j in range(len(list[i])):
				line = line + '{} | '.format(list[i][j])
			print(line)
			print('  -----------------------------------------')
			numberLine = ' '
			for i in range(10):
				numberLine = numberLine + '   ' + str(i+1)
		print(numberLine)
	botMines=[]

	def createMines(list,list1):
		x = random.randint(1,10)
		y = random.randint(1,10)
		if mineSweeper.isMined(x,y)==False:	
			list.append((x,y))
			list1.append((x-1,y-1))

	def createMinesLoop(list,list1):
		while len(ms.minesList) < 10:
			mineSweeper.createMines(list,list1)

	def isMined(x,y):
		return (x,y) in mineSweeper.minesList

	def numberOfMines(list):
		return len(minesList) 

	def surroundings(x,y):
		num = 0
		for i in range(-1,2):
			for j in range(-1,2):
				# print((x+i,y+j))
				if 10 >= x+i >=0 and 10>=y+j>=0 and (x+i,y+j) in mineSweeper.minesList:
					num=num+1
		return str(num)
		

	def inputCoordinate():
		try:
			xC = int(input('Please enter X coordinate to the map: \n'))
			yC = int(input('Please enter Y coordinate to the map: \n'))
			if (xC,yC) in mineSweeper.minesList:
				print('You are dead!')
				mineSweeper.endGame().status=True
			else:
				mineSweeper.revealNumber(xC,yC)

		except Exception as e:
			print('Please enter a valid coordinate!')
	def trueSightMap():	 	
	 	for (a,b) in mineSweeper.minesList:
	 		mineSweeper.TrueSight[9-(b-1)][a-1]='*'
	 	for i in range(len(mineSweeper.TrueSight)):
	 		for j in range(len(mineSweeper.TrueSight)):
	 			if mineSweeper.isMined(i+1,j+1)==False:
	 				mineSweeper.TrueSight[9-j][i]=mineSweeper.surroundings(i+1,j+1)
	 	return mineSweeper.TrueSight
	def actions():
	 	act = input('Please enter an action of your will: f for Flag, p for Place a point on the map, q for Quit Mine Sweeper: \n')
	 	if act.upper()=='F':
	 		mineSweeper.setFlag()
	 	elif act.upper()=='P':
	 		mineSweeper.inputCoordinate()
	 	elif act.upper()=='Q':
	 		mineSweeper.status=True
	 		print('End Game Now')
	 	elif act.upper()=='C':
	 		mineSweeper.cheat()
	 	elif act.upper()=='A':
	 		mineSweeper.aibot()
	 	elif act.upper()=='S':
	 		mineSweeper.solution()
	 		mineSweeper.layout(mineSweeper.botView)
	 		print(len(mineSweeper.flags))
	 	else:
	 		print('I cannot recongnize your command, please type correctly. \n')


	def run():
		mineSweeper.createMinesLoop(mineSweeper.minesList,mineSweeper.botMines)
		mineSweeper.trueSightMap()
		while mineSweeper.endGame()!=True:
			mineSweeper.layout(mineSweeper.empty)
			mineSweeper.actions()

	def setFlag():
		try:
			x = int(input('Enter X coordinate: \n'))
			y = int(input('Enter Y coordinate: \n'))
			mineSweeper.empty[9-(y-1)][x-1] = '?'
			flags.append((x,y))
		except Exception as e:
			print('Enter a valid coordinate.')

	def revealNumber(x,y):
			if mineSweeper.surroundings(x,y)=='0':
				mineSweeper.empty[9-(y-1)][x-1] = ' '
			else:
				mineSweeper.empty[9-(y-1)][x-1] = mineSweeper.trueSightMap()[9-(y-1)][x-1]
	def endGame():
		if mineSweeper.objective()==True:
			print('Congratz you won.')
			mineSweeper.status = True
			return mineSweeper.status
		return mineSweeper.status
	def objective():
		return mineSweeper.flags==mineSweeper.minesList and len(mineSweeper.flags) > 0
	def cheat():
		mineSweeper.layout(mineSweeper.trueSightMap())





	botView = []
	for i in range(10):
		botView.append([])
		for j in range(10):
			botView[i].append('#')
	calledCoordinate = []
	unknownCoordinate= []
	for i in range(0,10):
		for j in range(0,10):
			unknownCoordinate.append((i,j))

	def aibot():
		mineSweeper.layout(mineSweeper.trueSightMap())
		mineSweeper.botGetStartingCoordinate()
		while mineSweeper.status!=True:
			mineSweeper.solution()
			print('||||||')
		mineSweeper.layout(mineSweeper.empty)
		print(len(mineSweeper.flags))
	def botGetStartingCoordinate():
		for i in {0,9}:
			for j in {0,9}:
				mineSweeper.botGetCoordinate(i,j)

	def botGetCoordinate(x,y):
		mineSweeper.empty[9-y][x] = mineSweeper.trueSightMap()[9-y][x]
		mineSweeper.botView[9-y][x] = mineSweeper.trueSightMap()[9-y][x]
		temp = mineSweeper.trueSightMap()[9-y][x]
		if temp == '0' and (x,y) not in mineSweeper.calledCoordinate:
			mineSweeper.calledCoordinate.append((x,y))
			mineSweeper.unknownCoordinate.remove((x,y))
			for i in range(-1,2):
				for j in range(-1,2):
					if 10>x+i>=0 and 10>j+y>=0:
						mineSweeper.botGetCoordinate(x+i,y+j)
		elif temp != '0' and temp != '*' and (x,y) not in mineSweeper.calledCoordinate:
			mineSweeper.calledCoordinate.append((x,y))
			mineSweeper.unknownCoordinate.remove((x,y))
		elif temp =='*':
			mineSweeper.status=True
			print('Dead')


	def solution():
		new=0
		mineSweeper.checkNumber()
		for items in mineSweeper.calledCoordinate:
			a,b = items
			coordinate=(0,0)
			known=0
			if mineSweeper.botView[9-b][a]=='1':
				for p in mineSweeper.surroundingNumber(a,b):
					if p in mineSweeper.calledCoordinate:
						known+=1
					else:
						coordinate=p
						'''
						if there is only one unknown block around the selected block, and the number on the block is 1,then there must be a mine there
						when minus 1 must make sure the least number can have is 0
						after figure where the mine is, set a flag and put the coordinate of flag into called coordinates

						'''
				if known==(len(mineSweeper.surroundingNumber(a,b))-1) and (mineSweeper.toInt(a,b)>len(mineSweeper.nearByFlags(a,b))):
					x,y=coordinate
					mineSweeper.botSetFlag(x,y)
					mineSweeper.calledCoordinate.append((x,y))
					mineSweeper.unknownCoordinate.remove((x,y))
					new+=1
					'''
					 8 blocks around the flag, minus 1 to each of them
					'''
					for s in mineSweeper.surroundingNumber(x,y):
						if s in mineSweeper.calledCoordinate:
							try:
								mineSweeper.botView[9-s[1]][s[0]]=str(mineSweeper.botToInt(s[0],s[1])-1)
								mineSweeper.calledCoordinate.append((s[0],s[1]))
								mineSweeper.unknownCoordinate.remove((s[0],s[1]))
							except:
								print('.')

			if mineSweeper.botView[9-b][a]=='0':
				for s in mineSweeper.surroundingNumber(a,b):
					if s not in mineSweeper.calledCoordinate:
						mineSweeper.botAppend(s[0],s[1])
						mineSweeper.emptyAppend(s[0],s[1])
						mineSweeper.calledCoordinate.append(s)
						mineSweeper.unknownCoordinate.remove(s)
		mineSweeper.checkNumber()
		print(mineSweeper.unknownCoordinate)
		if new==0 and len(mineSweeper.unknownCoordinate)>0:
				print('now trying solve with probability')
				mineSweeper.checkNumber()
				mineSweeper.probabilitySolve()
				mineSweeper.layout(mineSweeper.empty)
		if new>0:
				mineSweeper.layout(mineSweeper.empty)
				print('execute solution again!')
				mineSweeper.solution()
				
		if len(mineSweeper.flags)==10:
			mineSweeper.status=True
			print('Think I am DONE')
			

	def probabilitySolve():
		mineSweeper.checkNumber()
		mineSweeper.clearZero()
		unknown=0
		prob=0
		unknowns={}
		unknownBlocks=[]
		highest=0
		f = (0,0)
		for p in mineSweeper.calledCoordinate:
			if p not in mineSweeper.flags:
				a,b=p
				if mineSweeper.botToInt(a,b)>0:
					'''
					find the unknown blocks and record the total number of them
					then record the coordinate with the number of mines around them to 'unknownBlocks'
					'''
					for s in mineSweeper.surroundingNumber(a,b):
						if s not in mineSweeper.calledCoordinate:
							unknown+=1
							unknownBlocks.append((s,mineSweeper.botToInt(a,b)))
				print('point {}: unknown numbers {}'.format(p,unknown))
				for p in unknownBlocks:
					coor,num = p
					x,y = coor
					unknowns.update({coor:prob})
					prob = (mineSweeper.botToInt(a,b) / unknown) * 10 + unknowns[coor]
					unknowns[coor]=prob
		for c in unknowns.keys():
			print('{}: probability {}'.format(c,unknowns[c]))			
			if unknowns[c]>highest:
				highest=unknowns[c]
				f = c

		mineSweeper.botSetFlag(f[0],f[1])
		mineSweeper.calledCoordinate.append(f)
		mineSweeper.unknownCoordinate.remove(f)
		mineSweeper.checkNumber()
		mineSweeper.clearZero()
		mineSweeper.checkMine()






	def surroundingNumber(x,y):
		sN = []
		for i in {-1,0,1}:
			for j in {-1,0,1}:
				if 10>x+i>=0 and 10>y+j>=0:
					sN.append((x+i,y+j))
					if x+i==x and y+j==y:
						sN.remove((x+i,y+j))
		return sN

	def botAppend(x,y):
		mineSweeper.botView[9-y][x]=mineSweeper.trueSightMap()[9-y][x]

	def emptyAppend(x,y):
		mineSweeper.empty[9-y][x]=mineSweeper.trueSightMap()[9-y][x]

	def nearByFlags(x,y):
		flagslist=[]
		for items in mineSweeper.surroundingNumber(x,y):
			a,b=items
			if items in mineSweeper.flags:
				flagslist.append(items)
		return flagslist

	def botSetFlag(x,y):
		mineSweeper.botView[9-y][x]='?'
		mineSweeper.empty[9-y][x]='?'
		mineSweeper.flags.append((x,y))

	def botToInt(x,y):
		return int(mineSweeper.botView[9-y][x])

	def toInt(x,y):
		return int(mineSweeper.trueSightMap()[9-y][x])

	def checkNumber():
		for points in mineSweeper.calledCoordinate:
			a,b=points
			if points not in mineSweeper.flags:
				if mineSweeper.toInt(a,b)-len(mineSweeper.nearByFlags(a,b))!=mineSweeper.botToInt(a,b):
					mineSweeper.botView[9-b][a]=str(mineSweeper.toInt(a,b)-len(mineSweeper.nearByFlags(a,b)))

	def clearZero():
		for items in mineSweeper.calledCoordinate:
			a,b=items
			if mineSweeper.botView[9-b][a]=='0':
				for s in mineSweeper.surroundingNumber(a,b):
					if s not in mineSweeper.calledCoordinate:
						mineSweeper.botAppend(s[0],s[1])
						mineSweeper.emptyAppend(s[0],s[1])
						mineSweeper.calledCoordinate.append(s)
						mineSweeper.unknownCoordinate.remove(s)	
	def checkMine():
		for i in mineSweeper.calledCoordinate:
			a,b=i
			if mineSweeper.botView[9-b][a]=='*':
				print('you are ded')
				mineSweeper.status=True



ms = mineSweeper
ms.run()
