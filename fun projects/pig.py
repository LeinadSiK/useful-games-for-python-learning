import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit() and int(players) >= 1 and int(players) < 5:
        players = int(players)
        break
    else:
        print("Invalid input, players must be between 2 and 4.")
        continue
        

max_score = 21
player_scores = [0 for _ in range(players)]
game_is_running = True
max_rolls = 3
rolls = 0

def play_game():
    while game_is_running:
        for player_idx in range(players):          
            print("\nPlayer", player_idx + 1,", it's your turn.\n")
            print("Your score is", player_scores[player_idx],"\n")
            
            rolls = 0
                    
            while rolls < max_rolls:
                should_roll = input("Press Enter to roll.\n")
                value = roll()
                current_score = 0
                rolls += 1

                if value == 1:
                        player_scores[player_idx] = 0 #current_score = 0
                        print("You rolled a 1, you're back to 0, your turn is over.\n")
                        break

                else:
                        current_score += value
                        player_scores[player_idx] += current_score 
                        realTime_score = player_scores[player_idx]
                        print("You rolled a", value,", your current score is", realTime_score, "\n")
                
                if player_scores[player_idx] == max_score:
                        print("Player", player_idx + 1, "wins!")                  
                        return
                        
                        
                elif player_scores[player_idx] > max_score:
                            print("You went over 21, your score is reset to 0.")
                            player_scores[player_idx] = 0
                            break
                    
            print("The scoreboard is:")
            print(player_scores)                
        
play_game()


            #print("Your score is", player_scores[player_idx])

        
#max_score = max(player_scores)
#winning_idx = player_scores.index(max_score)
#print("Player", winning_idx + 1, "won with a score of", max_score)

# I need to get exactly 21 to win
# I can roll the dice three times except if I roll a 1
# If I roll a 1 I lose all my points and my turn is over
# If I roll a 1 I can't roll again in that turn
# the total of my current score is added to my total score
# if I go over 21, the total score is reset to 0 and my turn is over

