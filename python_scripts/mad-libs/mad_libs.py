with open("story.txt", "r") as f:
    story = f.read()

# This gets a "slice" of the string from ["beginning_char_index":"ending_char_index"]
#print(story[140:166])

# Create an empty list for words
words = []
# Use this to ensure the beginning delimeter was found before the end delimeter
start_of_word = -1

start_delim = "<"
end_delim = ">"

# Use enumerate to get the character as well as the position (i) of the character
for i, char in enumerate(story):
    if char == start_delim:
        # Get the index of the starting delimeter
        start_of_word = i
    # Make sure the end delimeter also has a beginning delimeter to pair with it
    if char == end_delim and start_of_word != -1:
        # Get a slice of the string from the beginning index to the ending index + 1 (to include the final character)
        word = story[start_of_word: i + 1]
        # Add the word to the words list
        words.append(word)
        # Set this back -1 to help pair with the end delimeter again
        start_of_word = -1

# Create an empty dictionary
answers = {}

# Get a word to store in the answers dictionary
for word in words:
    answers[word] = input(f"Enter a word for {word}: ")

# Replace each word in the story with the corresponding dictionary entry in "answers"
for word in words:
    story = story.replace(word, answers[word])

print(story)