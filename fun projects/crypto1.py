# Caesar Cipher
import random

symbol_sets = {'latin':'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
               'cyrillic':'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмно',
               'chinese' : '朋风水笑心明青鸟山花云路天月星林雨雪火石竹眼手足木金土空音乐色声刀剑盾羽光影琴画文字笔书等问答笑泪望梦眠'} #прстуфхцчшщьюя
#SYMBOLS = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
#LATIN_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def getMode():
    while True:
        print('Would you like to encrypt or decrypt?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print("Enter either 'encrypt' (e) or 'decrypt' (d).")

def getSymbolSetName(symbol_sets, messages):
    notFoundSymbolSet = True
    messageTracker = 0
    keyIndex = 0
    list_of_symbol_sets = ''
    for key in symbol_sets.keys():
        list_of_symbol_sets = list_of_symbol_sets + key

        if keyIndex < len(symbol_sets.keys()) - 1:
            list_of_symbol_sets = list_of_symbol_sets + ' or '
        keyIndex += 1


    while notFoundSymbolSet:
        print(messages[messageTracker] + list_of_symbol_sets)
        userInput = input()
        userInput = userInput.strip()
        if userInput in symbol_sets:
            notFoundSymbolSet = False
        else:
            messageTracker = 1
    return userInput

def getMessage():
    print('Enter your message:')
    return input()

def getKey(symbol_sets):
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (len(symbol_sets)))
        key = int(input())
        if (key >= 1 and key <= len(symbol_sets)):
            return key
        

def getTranslatedMessage(mode, message, key, startingSymbols, goalSymbols):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        
        symbolIndex = startingSymbols.find(symbol)

        if symbolIndex == -1: # Symbol not found in SYMBOLS. This means that any characters that aren’t part of the alphabet, such as commas and periods, won’t be changed and are added to the translated text.
            #Just add the -1 symbol without any changes.
            translated += symbol
        else:
            #Encrypt or decrypt.
            symbolIndex += key

            if symbolIndex >= len(goalSymbols):
                symbolIndex -= len(goalSymbols)
            elif symbolIndex < 0:
                symbolIndex += len(goalSymbols)

            translated += goalSymbols[symbolIndex]
    return translated


mode = getMode()
startingSymbols = getSymbolSetName(symbol_sets,['Please enter the starting symbol set: ', 'Symbol set does not exist, please enter a new one.'])
goalSymbols = getSymbolSetName(symbol_sets, ['Please enter the goal symbol set: ', 'Symbol set does not exist, please enter a new one.'])
message = getMessage()   
key = getKey(symbol_sets[startingSymbols])

print('Your translated text is:')
print(getTranslatedMessage(mode, message, key, symbol_sets[startingSymbols], symbol_sets[goalSymbols]))
