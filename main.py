import time
import subprocess

# Function to play Morse code using audio files (dot.wav and dash.wav)
def play_morse_code(morse_code, dot_duration=100):
    for symbol in morse_code:
        if symbol == '.':
            subprocess.call(["afplay", "tex_to_morse_code/dot.wav"])  # Play dot sound
            time.sleep(dot_duration / 1000)  # Pause for a dot duration
        elif symbol == '-':
            subprocess.call(["afplay", "tex_to_morse_code/dash.wav"])  # Play dash sound
            time.sleep(dot_duration / 1000 * 3)  # Dash is 3x longer than dot
        elif symbol == ' ':
            time.sleep(dot_duration / 1000 * 3)  # Space between letters
        elif symbol == '/':
            time.sleep(dot_duration / 1000 * 7)  # Space between words

# Binary Tree Node class for decoding Morse code
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None   # Dash branch
        self.right = None  # Dot branch

# Root of the Morse decoding tree
root = Node('Start')

# Building the left (dash-heavy) subtree of the Morse code binary tree
root.left = Node('T')
root.left.left = Node('M')
root.left.left.left = Node('O')
root.left.left.right = Node('G')
root.left.right = Node('N')
root.left.right.left = Node('K')
root.left.right.left.left = Node('Y')
root.left.right.left.right = Node('C')
root.left.right.right = Node('D')
root.left.right.right.left = Node('X')
root.left.right.right.right = Node('B')

# Building the right (dot-heavy) subtree of the Morse code binary tree
root.right = Node('E')
root.right.left = Node('A')
root.right.left.left = Node('W')
root.right.left.left.left = Node('J')
root.right.left.left.right = Node('P')
root.right.left.right = Node('R')
root.right.left.right.right = Node('L')
root.right.right = Node('I')
root.right.right.left = Node('U')
root.right.right.left.left = Node('-')  # Maybe used as filler or separator
root.right.right.left.right = Node('F')
root.right.right.right = Node('S')
root.right.right.right.left = Node('V')
root.right.right.right.right = Node('H')

# Dictionary mapping letters to their Morse code representation
words = {
    "A": ".-",    "B": "-...",  "C": "-.-.", "D": "-..",   "E": ".",
    "F": "..-.",  "G": "--.",   "H": "....", "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",   "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",  "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",  "X": "-..-",  "Y": "-.--",
    "Z": "--..",  " ": "/"
}

# Convert Morse code back into human-readable word(s)
def code_to_word(text):
    word = ""
    direction = root  # Start at root each time

    for char in text:
        if char == '.':
            direction = direction.right  # Dots go right
        elif char == '-':
            direction = direction.left   # Dashes go left
        elif char == '/':  # Word separator
            if direction != root:
                word += direction.value
            word += " "
            direction = root
        elif char == ' ':  # Letter separator
            if direction != root:
                word += direction.value
                direction = root
        else:
            raise Exception("Only dots and dashes allowed in Morse code.")  # Input error check

    # If we end mid-character, still append it
    if direction != root:
        word += direction.value

    print(f"the word is: { word.replace('Start', ' ') }")

# Convert text to Morse code and play the corresponding sounds
def word_to_code(text):
    morse_code = ""
    for c in text:
        morse_code += words[c] + " "  # Add Morse code for each character with space

    print(f"the code is: { morse_code.strip()}")

    play_sound = input("Would you like to play the sound?(Enter Yes or No): ").lower()

    if play_sound == "yes":
        play_morse_code(morse_code.strip())  # Play the sound for the generated code

# Get input from the user and determine if it's Morse code or plain text
text = input('Enter Morse code or text : ').upper()

if "-" in text or "." in text:
    # If input contains dots or dashes, treat it as Morse
    code_to_word(text)
else:
    # Otherwise, treat it as plain text to encode
    word_to_code(text)
