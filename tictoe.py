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

"""
Main Program Starting
"""
origin_board = [0,1,2,3,4,5,6,7,8,]
ai_player = 'X'
human_player = 'O'
while(True):
	available =empty_list(origin_board)
	print("Human Turn")
	print("Select one Among the below indeces")
	print(available)
	index_choosen = int(input())
	origin_board[index_choosen] = 'O'
	for i in range(len(origin_board)):
		print(origin_board[i],end = " ")
		if(i == 2 or i == 5 or i == 8):
			print("\n")
	best_spot = minimax(origin_board,ai_player)
	#print(best_spot)
	key = list(best_spot.keys())
	if(key[0] != 'score'):
		origin_board[key[0]] = 'X'
	print("AI Turn")
	for i in range(len(origin_board)):
		print(origin_board[i],end = " ")
		if(i == 2 or i == 5 or i == 8):
			print("\n")
	available = empty_list(origin_board)
	if(winning_combination(origin_board,ai_player)):
		print("Computer Won")
		break
	elif(winning_combination(origin_board,human_player)):
		print("You Won")
		break
	elif(len(available) == 0):
		print("Tie")
		break
