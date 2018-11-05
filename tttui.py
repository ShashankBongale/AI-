import pygame
import sys
import time
def rc_to_r(r,c):
	if(r == 0 and c == 0):
		res = 0
	elif(r == 0 and c == 1):
		res = 1
	elif(r == 0 and c == 2):
		res = 2
	elif(r == 1 and c == 0):
		res = 3
	elif(r == 1 and c == 1):
		res = 4
	elif(r == 1 and c == 2):
		res = 5
	elif(r == 2 and c == 0):
		res = 6
	elif(r == 2 and c == 1):
		res = 7
	elif(r == 2 and c == 2):
		res = 8
	return res
def r_to_rc(row):
	if(row == 0):
		r = 0
		c = 0
	elif(row == 1):
		r = 0
		c = 1
	elif(row == 2):
		r = 0
		c = 2
	elif(row == 3):
		r = 1
		c = 0
	elif(row == 4):
		r = 1
		c = 1
	elif(row == 5):
		r = 1
		c = 2
	elif(row == 6):
		r = 2
		c = 0
	elif(row == 7):
		r = 2
		c = 1
	elif(row == 8):
		r = 2
		c = 2
	return (r,c)
def boardPos (mouseX, mouseY):
    if (mouseY < 100):
        row = 0
    elif (mouseY < 200):
        row = 1
    else:
        row = 2
    if (mouseX < 100):
        col = 0
    elif (mouseX < 200):
        col = 1
    else:
        col = 2
    return (row, col)
def drawMove(board,row,col,player):
	print(player)
	centerX = ((col) * 100) + 50
	centerY = ((row) * 100) + 50
	if(player == 'O'):
		pygame.draw.circle (board, (100,149,237), (centerX, centerY),20, 20)
	else:
		print("Inside draw")
		pygame.draw.line (board, (100,149,237), (centerX - 22, centerY - 22),(centerX + 22, centerY + 22),15)
		pygame.draw.line (board, (100,149,237), (centerX + 22, centerY - 22),(centerX - 22, centerY + 22),15)
def clickBoard(board,player):
	(mouseX, mouseY) = pygame.mouse.get_pos()
	(row, col) = boardPos(mouseX, mouseY)
	return (row,col)
def empty_list(new_board):
	l = []
	for i in new_board:
		if(i != 'X' and i != 'O'):
			l.append(i)
	return l
def winning_combination(board,player):
	if((board[0] == player and board[1] == player and board[2] == player) or
	(board[3] == player and board[4] == player and board[5] == player) or
	(board[6] == player and board[7] == player and board[8] == player) or
	(board[0] == player and board[3] == player and board[6] == player) or
	(board[1] == player and board[4] == player and board[7] == player) or
	(board[2] == player and board[5] == player and board[8] == player) or
	(board[0] == player and board[4] == player and board[8] == player) or
	(board[2] == player and board[4] == player and board[6] == player)
	):
		return True
	else:
		return False
def minimax(new_board,player):
	available_index = empty_list(new_board)
	if(winning_combination(new_board,human_player)):
		return ({'score':-10})
	elif(winning_combination(new_board,ai_player)):
		return ({'score':10})
	elif(len(available_index) == 0):
		return ({'score':0})
	moves = []
	for i in range(len(available_index)):
		move = {}
		new_board[available_index[i]] = player
		if(player == ai_player):
			result = minimax(new_board,human_player)
			#print("Result",result)
			key = list(result.keys())
			move[available_index[i]] = result[key[0]]
		else:
			result = minimax(new_board,ai_player)
			#print("Result",result)
			key = list(result.keys())
			move[available_index[i]] = result[key[0]]
		new_board[available_index[i]] = available_index[i]
		moves.append(move)
	#print("Moves",moves)
	temp = []
	for i in moves:
		temp.append(list(i.keys()))
	keys = []
	for i in temp:
		for j in i:
			keys.append(j)
	if(player == ai_player):
		best_score = -10000
		for i in range(len(moves)):
			if(moves[i][keys[i]] > best_score):
				best_score = moves[i][keys[i]]
				best_move = i
	else:
		best_score = 10000
		for i in range(len(moves)):
			if(moves[i][keys[i]] < best_score):
				best_score = moves[i][keys[i]]
				best_move = i
	return moves[best_move]
def show_message(background,text):
	if(text == "Computer Won"):
		background_colour = (255,0,0)
		font_colour = (0,0,0)
	else:
		background_colour = (255,140,0)
		font_colour = (65,105,225)
	pygame.display.update()
	background.fill(background_colour)
	largetext = pygame.font.Font('/home/shashank/Desktop/AI/font/Action_Man.ttf',35)
	TextSurf = largetext.render(text,True,font_colour)
	TextRect = TextSurf.get_rect()
	TextRect.center = ((150,150))
	background.blit(TextSurf,TextRect)
	pygame.display.update()

"""
Main Program Startting
"""
origin_board = [0,1,2,3,4,5,6,7,8]
ai_player = 'X'
human_player = 'O'
"""
Building board
"""
mark_array = [0,0,0,0,0,0,0,0,0]
pygame.init()
background = pygame.display.set_mode((300,300))
pygame.display.set_caption("Hello World")
background.fill((255,235,205))
pygame.draw.line (background, (0,0,0), (100, 0), (100, 300), 2)
pygame.draw.line (background, (0,0,0), (200, 0), (200, 300), 2)
pygame.draw.line (background, (0,0,0), (0, 100), (300, 100), 2)
pygame.draw.line (background, (0,0,0), (0, 200), (300, 200), 2)
pygame.draw.line (background, (0,0,0), (0, 300), (300, 300), 2)

while(True):
	available = empty_list(origin_board)
	for event in pygame.event.get():
		#print(event)
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()
		elif event.type is pygame.MOUSEBUTTONDOWN:
			(row,col) = clickBoard(background,human_player)
			r = rc_to_r(row,col)
			if(mark_array[r] == 0):
				origin_board[r] = 'O'
				drawMove (background, row, col,human_player)
				pygame.display.update()
				time.sleep(0.3)
				best_spot = minimax(origin_board,ai_player)
				key = list(best_spot.keys())
				print(key)
				if(key[0] != 'score'):
					origin_board[key[0]] = 'X'
					mark_array[key[0]] = 1
					(row,col) = r_to_rc(key[0])
					drawMove(background,row,col,ai_player)
					pygame.display.update()
				available = empty_list(origin_board)
				if(winning_combination(origin_board,ai_player)):
					print("Computer Won")
					text = "Computer Won"
					pygame.display.update()
					time.sleep(0.9)
					show_message(background,text)
					time.sleep(2)
					pygame.quit()
					sys.exit()
				elif(winning_combination(origin_board,human_player)):
					print("You Won")
					time.sleep(1)
					pygame.quit()
					sys.exit()
				elif(len(available) == 0):
					print("Tie")
					text = "Tie"
					pygame.display.update()
					time.sleep(0.9)
					show_message(background,text)
					time.sleep(2)
					pygame.quit()
					sys.exit()
				mark_array[r] = 1
	pygame.display.update()
