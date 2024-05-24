with open("story.txt", "r") as f:
    story = f.read()

#print("\n", story, "\n")

words = set()
start_of_word = -1

for i, character in enumerate(story):
    if character == "<":
        start_of_word = i 

    elif character == ">" and start_of_word != -1: 
        #words.append(story[start_of_word + 1:i])
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print("\n", story, "\n")
