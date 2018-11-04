import pygame
import sys
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
def drawMove(board,row,col):
	centerX = ((col) * 100) + 50
	centerY = ((row) * 100) + 50
	#pygame.draw.circle (board, (100,149,237), (centerX, centerY),20, 20)
	pygame.draw.line (board, (100,149,237), (centerX - 22, centerY - 22),(centerX + 22, centerY + 22),15)
	pygame.draw.line (board, (100,149,237), (centerX + 22, centerY - 22),(centerX - 22, centerY + 22),15)

def clickBoard(board):
	(mouseX, mouseY) = pygame.mouse.get_pos()
	(row, col) = boardPos(mouseX, mouseY)
	drawMove (board, row, col)
pygame.init()
background = pygame.display.set_mode((300,300))
pygame.display.set_caption("Hello World")
background.fill((255,235,205))
pygame.draw.line (background, (0,0,0), (100, 0), (100, 300), 2)
pygame.draw.line (background, (0,0,0), (200, 0), (200, 300), 2)
pygame.draw.line (background, (0,0,0), (0, 100), (300, 100), 2)
pygame.draw.line (background, (0,0,0), (0, 200), (300, 200), 2)
while(True):
	for event in pygame.event.get():
		#print(event)
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()
		elif event.type is pygame.MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
			clickBoard(background)
	pygame.display.update()
