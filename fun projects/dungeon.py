import random
import keyboard
import sys
import time

tile_one = '.'
row_one = [tile_one,".",".","."]


room_one = [[".",".",".",".",".",".",".","."],
           [".",".",".",".",".",".",".","."],
           [".",".",".",".",".",".",".","."],
           [".",".",".",".", ".",".",".","."],
           [".",".",".",".",".",".",".","."]]

#room_one[0][0] == row_one[0]
#print(room_one[1][1]) - multidimensional list explanation

def generate_character():
    character = [2, 0]
    return character

def print_room(room_one, character, character_icon):
    for row_index in range(len(room_one)): 
        for tile_index in range(len(room_one[row_index])):
            if [row_index, tile_index] == character:
                print(character_icon, end=' ')
            else:
                print(room_one[row_index][tile_index], end=' ')
        print()

def move_character(character):
    new_character = []
    direction = keyboard.read_key(suppress=True)    
    if direction == 'up':
        new_character = [character[0] - 1, character[1]]
    elif direction == 'down':
        new_character = [character[0] + 1, character[1]]
    elif direction == 'left':
        new_character = [character[0], character[1] - 1]
    elif direction == 'right':
        new_character = [character[0], character[1] + 1]
    

    return new_character    


character_icon = '🎃'    
character = generate_character() 
isFirstMove = True

def collapseRoom(room_one):
    room_height = len(room_one)
    room_width = len(room_one[0])
    random_row = random.randint(0, room_height - 1)
    random_column = random.randint(0, room_width - 1)
    if room_one[random_row][random_column] == '.':
        room_one[random_row][random_column] = 'X'

        # continuar here


Game_is_running = True
last_position = list(character)
while Game_is_running:    
    if isFirstMove: 
        print("Press enter to begin")
        wait = input()
        print("Press arrows to move character")    
        isFirstMove = False

    print_room(room_one, character, character_icon)
    print()
    print()
    last_position = list(character)
    character = move_character(character)
    time.sleep(0.1)
    room_one = collapseRoom(room_one)

    if character[0] < 0 or character[0] > 4 or character[1] < 0 or character[1] > 7:
        
        character = last_position
        character_icon = '💥'
        print_room(room_one, character, character_icon)
        print("You have left the room")
        Game_is_running = False
        


    # sys.exit()

    #keyboard.read_key()

#room_one[0] == row_one
        
        # What could be done:
        # get a timer
        # have the character move around the room
        # reach a point by avoiding obstacles
        # have a timer
        # have a score
        # have a way to win
        # have a way to lose
        # have a way to restart
        # have a way to quit
        # have a way to pause
        # the concept could be that you are a character trying to get to a certain point in the room
        # and tiles are disappearing randomly, and you cannot step on them, only on dots and have to reach a certain point before time runs out
        #define the destination that must be reached
        #make sure that it is achievable
        #make sure that it is not too easy
        #make sure that it is not too hard
        #make sure that it is random