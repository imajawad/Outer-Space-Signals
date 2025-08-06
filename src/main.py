import os
from collections import Counter

#Load the signal from the text file
signal_path = "../signal.txt"
with open(signal_path, "r") as f:
    signal_text = f.read()

# Display the length of the signal loaded
print(f"Loaded signal.txt with {len(signal_text)} characters.")


TARGET_LENGTH = 721 
TOP_ENGLISH_LETTERS = list("ETAOIRSNHU")  # Top 10 frequent letters in English text

best_window = ""  # Will store the best match for the encrypted message
best_score = 0  # Will store the highest frequency score

# Loop through the signal to find the 721-character window that best matches English frequencies
for i in range(len(signal_text) - TARGET_LENGTH + 1):
    window = signal_text[i:i + TARGET_LENGTH]  # Get a slice of 721 characters
    letters_only = window.replace(" ", "")  # Remove spaces to focus only on letters
    
    # Count the frequency of each letter in this window
    freq = Counter(letters_only)
    
    # Get the top 10 most common letters
    most_common = [letter for letter, _ in freq.most_common(10)]
    
    # Score how many of the top English letters are in this window
    score = len(set(most_common) & set(TOP_ENGLISH_LETTERS))
    
    # If this window scores better, remember it as the best window
    if score > best_score:
        best_score = score
        best_window = window

# Show the best score we found and the corresponding encrypted message window
print("\nBest score:", best_score)
print("\nCandidate encrypted message:")
print(best_window)

#Frequency analysis for substitution cipher
# We define the standard English letter frequency order
ENGLISH_FREQ_ORDER = list("ETAOIRSNHLDCMFYWGPBVKXQJZ")

# Analyze the character frequency in the best matching window
cipher_only = best_window.replace(" ", "")  # Remove spaces from the window
cipher_freq = Counter(cipher_only)  # Count frequency of each letter
cipher_sorted = [letter for letter, _ in cipher_freq.most_common()]  # Sort letters by frequency

# Map the most common letters in the cipher to the most common letters in English
substitution_map = dict(zip(cipher_sorted, ENGLISH_FREQ_ORDER))

# Display the tentative substitution map (letter by letter)
print("\nTentative Substitution Map:")
for cipher_char, english_char in substitution_map.items():
    print(f"{cipher_char} -> {english_char}")

#Decrypt the message using the substitution map
decrypted_message = ""  # This will store the decrypted message

# Replace each character in the best window using the substitution map
for char in best_window:
    if char == " ":  # Keep spaces intact
        decrypted_message += " "
    else:
        # Decrypt using the substitution map; use "?" if no substitution is found
        decrypted_message += substitution_map.get(char, "?")

# Show the partially decrypted message (still has some unknowns)
print("\nPartially Decrypted Message\n")
print(decrypted_message)

#Extract the first 9 words from the decrypted message
first_9_words = decrypted_message.split()[:9]

# Show the first 9 words (which are required for submission)
print("\nFirst 9 Words\n")
print(" ".join(first_9_words))
