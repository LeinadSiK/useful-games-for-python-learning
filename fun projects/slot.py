import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = { "☢️" : 2, "💣" : 4,  "🚀" : 6, "👽" : 8}

symbol_value = { "☢️" : 5, "💣" : 4,  "🚀" : 3, "👽" : 2}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if 0 < amount <= 200:
#                print("You have deposited $" + str(amount) + ".")
                break
            else: print("Please enter a number greater than 0 but not greater than 200.")
        else: print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else: print("Please enter a number between 1 and " + str(MAX_LINES) + ".")

    return lines

def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: print("Please enter an amount between " + str(MIN_BET) + " and " + str(MAX_BET) + ".")
    return amount

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else: print("""You don't have enough money to make that bet.
                    Your balance is: $ """ + (str(balance)) + ".")
    
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Your total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines, sep=", ")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
       print(f"Your balance is: ${balance}")
       spin = input("Press Enter to play (q to quit): ")
       if spin == "q":
           break
       balance += game(balance)
       if balance <= 0:
           print("You have no more money to play with.")
           break
    print(f"Your final balance is: ${balance}.")

main()