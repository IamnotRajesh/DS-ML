def word_pyramid_up(word):
    # Iterate through each character of the word
    for i in range(len(word)):
        # Print spaces for alignment
        print(" " * (len(word) - i - 1), end="")
        # Print the characters of the word from the beginning up to the ith character
        print(' '.join(word[:i+1]))

def word_pyramid_down(word):
    # Iterate through each character of the word in reverse order
    for i in range(len(word), 0, -1):
        # Print spaces for alignment
        print(" " * (len(word) - i), end="")
        # Print the characters of the word from the beginning up to the ith character
        print(' '.join(word[:i]))

# Get user input for the word
user_input = input("Enter a word: ")

# Get user input for the direction
direction = input("Enter 'up' for upward direction or 'down' for downward direction: ")

if direction.lower() == "up":
    word_pyramid_up(user_input)
elif direction.lower() == "down":
    word_pyramid_down(user_input)
else:
    print("Invalid direction input. Please enter 'up' or 'down'.")


