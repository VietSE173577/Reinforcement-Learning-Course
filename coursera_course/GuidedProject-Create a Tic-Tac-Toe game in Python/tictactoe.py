# Import numpy as np
import numpy as np
import pygame
import math

# Define constants
ROWS = 3
COLUMNS = 3

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH,HEIGHT)
CIRCLE = pygame.transform.scale(pygame.image.load('circle.png'), (100, 100))
CROSS = pygame.transform.scale(pygame.image.load('x.png'), (100, 100))
# Function to mark a position on the board
def mark(row, col, player):
    board[row][col] = player

# Function to check if a move is valid
def is_valid_mark(row, col):
    return board[row][col] == 0

# Function to check if a board is full
def is_board_full():
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == 0:
                return False
    return True

def draw_board():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 1:
                window.blit(CROSS, ((c * 200) + 50, (r * 200) + 50))
            elif board[r][c] == 2:
                window.blit(CIRCLE, ((c * 200) + 50, (r * 200) + 50))
    pygame.display.update()

# Function to draw the tic-tac-toe grid lines
def draw_lines():
    # Vertical lines
    pygame.draw.line(window, BLACK, (200, 0), (200, 600), 10)
    pygame.draw.line(window, BLACK, (400, 0), (400, 600), 10)
    
    # Horizontal lines
    pygame.draw.line(window, BLACK, (0, 200), (600, 200), 10)
    pygame.draw.line(window, BLACK, (0, 400), (600, 400), 10)

# Function to check if a player has won
def is_winning_move(player):
    if player == 1:
        winning_color = RED
    else:
        winning_color = BLUE
    
    # Check rows
    for r in range(ROWS):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            pygame.draw.line(window, winning_color, (10, (r * 200) + 100), (WIDTH - 10, (r * 200) + 100), 10)
            return True
    
    # Check columns
    for c in range(COLUMNS):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            pygame.draw.line(window, winning_color, ((c * 200) + 100, 10), ((c * 200) + 100, HEIGHT - 10), 10)
            return True
    
    # Check main diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        pygame.draw.line(window, winning_color, (10, 10), (590, 590), 10)
        return True
    
    # Check other diagonal
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        pygame.draw.line(window, winning_color, (590, 10), (10, 590), 10)
        return True
    
    return False

# Initialize the board with zeros
board = np.zeros((ROWS, COLUMNS))
game_over = False
turn = 0

pygame.init()
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption('tic tac toe')
window.fill(WHITE)
draw_lines()
pygame.display.update()
pygame.time.wait(2000)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if turn % 2 == 0:  # Player 1
                row = int(event.pos[1] // 200)
                col = int(event.pos[0] // 200)
                if is_valid_mark(row, col):
                    mark(row, col, 1)
                    if is_winning_move(1):
                        game_over = True
                else:
                    turn -= 1
            else:  # Player 2
                row = int(event.pos[1] // 200)
                col = int(event.pos[0] // 200)
                if is_valid_mark(row, col):
                    mark(row, col, 2)
                    if is_winning_move(2):
                        game_over = True
                else:
                    turn -= 1
            
            turn += 1
            print(board)
            draw_board()
    if game_over==True:
        print('Game Over')
        pygame.time.wait(2000)
        board.fill(0)
        window.fill(WHITE)
        draw_lines()
        draw_board()
        game_over=False
        pygame.display.update()