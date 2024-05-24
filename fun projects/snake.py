#Board 20x20, touching edges kills player, randomly spawning apples, counting score
#snake needs to grow after eating apple, player controls snake movement, game ends when player dies

from os import remove
import random
import time
import keyboard

def generateBoard(width,height,character):
    board = []
    board_line = []
    x_index = 0
    y_index = 0

    while x_index < width:
        while y_index < height:
            board_line.append(character)
            y_index = y_index + 1
        board.append(board_line)
        board_line = []
        y_index = 0
        x_index = x_index + 1

    return board

def printBoard(board, snake, food):
    for x_index in range(len(board)):
        for y_index in range(len(board[x_index])):
            printedSnake = False
            printedRat = False
            for snakePart in snake:
                if len(snakePart) >= 2 and snakePart[0] == x_index and snakePart[1] == y_index:
                    print(snakePart[2], end='') 
                    printedSnake = True   
                    
                    
            
            if not printedSnake:
                for ratPart in food:
                    if ratPart[0] == x_index and ratPart[1] == y_index:
                        print(ratPart[2], end='')
                        printedRat = True

                if not printedRat: 
                    print(board[x_index][y_index], end=' ')
                           
        print()


def generateStartingSnake(height_of_room, lenght_of_room):
    snake = []
    snake.append([random.randint(1,height_of_room-2), random.randint(1,lenght_of_room-2), '🐲'])

    return snake


def getNewBoard(row,column,character):
    board = []
    for x in range(row):
        board.append([])
        for y in range(column): 
            board[x].append(character)
            
    return board

def getNewRat(snake):
    rat = []
    while True:
        newRat = [random.randint(0, 7), random.randint(0, 7), '🐁']
        if  newRat not in rat and newRat not in snake:
            rat.append(newRat)
            
        return rat
    

def moveSnake(snake):    # I want the snake to move according to key commands and reprint the board. 
    newSnake = []           # Last position of snake should be green circle.
    while True:
        direction = keyboard.read_key(suppress=True)
        if direction == 'up':
            newSnake = [snake[0][0] - 1, snake[0][1], '🐲']  # Move up
        elif direction == 'down':
            newSnake = [snake[0][0] + 1, snake[0][1], '🐲']  # Move down
        elif direction == 'left': 
            newSnake = [snake[0][0], snake[0][1] - 1, '🐲']  # Move left
        elif direction == 'right':
            newSnake = [snake[0][0], snake[0][1] + 1, '🐲']  # Move right   

        for i in range(len(snake) - 1, 0, -1): # Get to second+ item in snake list and update with each last position of snakehead.        
            snake[i] = list(snake[i - 1])
            snake[i][2] = '🟢'
        
        snake[0] = newSnake

        
        return snake # !!!!major problem here, the snake last segment is inserted as last position, then copies the second segment, thus will have the exact same position as the second segment.
    
        
def gulp(snake, food):
    
    if snake and food and isinstance(snake[0], list) and isinstance(food[0], list):
        if snake[0][0] == food[0][0] and snake[0][1] == food[0][1]:  # - ['🐲'] - ['🐁']
            del (food[0])
            growSnake(snake, last_position)            
        return True
    
    else:          
        return False
    
def growSnake(snake, newSegment):
    
    newSegment = list(last_position)
    newSegment[2] = '🟢'
    if 0 <= last_position[0] < 8 and 0 <= last_position[1] < 8:  # Check if the new segment would be off the board
        snake.append(newSegment)
    
    return snake



isGameStillGoing = True
snake = generateStartingSnake(8,8)
food = getNewRat(snake)
gameBoard = getNewBoard(8,8,'.',)
isFirstMove = True


while isGameStillGoing:
    
    printBoard(gameBoard, snake, food)
    print('Score: ' + str(len(snake) - 1))
    
    if isFirstMove:
        print('Press Enter to begin game.')
        wait = input()
        print('Press arrow keys to move snake.')
        isFirstMove = False
    
    last_position = list(snake[-1])
    snake = moveSnake(snake)
    time.sleep(0.2)
    gulp(snake, food)
    if food == []:
        food = getNewRat(snake)

    
    if snake[0][0] == -1 or snake[0][0] == 8 or snake[0][1] == -1 or snake[0][1] == 8:
        print('💀')
        print('You died.')     
        
        if 0 <= last_position[0] <= 7 and 0 <= last_position[1] <= 7:
            gameBoard[last_position[0]][last_position[1]] = '💀'
            for segment in snake:  # Add this loop
                segment[2] = '💀'
        printBoard(gameBoard, snake, food)
        isGameStillGoing = False

    for segment in snake[1:]:
        if snake[0][0] == segment[0] and snake[0][1] == segment[1]:
            print('💀')
            print('You died.')            
            gameBoard[snake[0][0]][snake[0][1]] = '💀'
            for segment in snake:  # Add this loop
                segment[2] = '💀'
            printBoard(gameBoard, snake, food)
            isGameStillGoing = False
            break

        if last_position == segment[0] and last_position == segment[1]:
            print('💀')
            print('You died.')            
            gameBoard[snake[0][0]][snake[0][1]] = '💀'
            for segment in snake:  # Add this loop
                segment[2] = '💀'
            printBoard(gameBoard, snake, food)
            isGameStillGoing = False




