########################################################
# Software Req Doc: HW8 Working with Files in Python   #
# Release Date: October 12, 2026                       #
# Coder: Alexis Barraza                                #
# Description: Reads and analyzes a Ceaser cipher file.#
########################################################


def main():
    """Reading text file and displaying cipherJA.txt"""
    
    with open("cipherJA.txt", "r") as file:
        cja = file.read()
        
    # Requirement 2
    print(cja)
    
    # Requirement 3
    ja_analysis = letter_count(cja)
    
    print("\n --- Letter Counts ---")
    
    for letter, count in sorted(ja_analysis.items()):
        print(f"{letter}: {count}")
    
    # Step 3.6: Find the letter that appears the most.
    most_common_letter = ""
    highest_count = 0
    
    for letter, count in ja_analysis.items():
        if count > highest_count:
            highest_count = count
            most_common_letter = letter
    
    print("\n--- Most Common Letter ---")
    print(f"Most common letter: {most_common_letter}")
    print(f"Count: {highest_count}")
    
    shift = ord('e') - ord(most_common_letter)
    print(f"Shift from e: {shift}")
    
    deciphered_text = caesar_cipher(cja, shift)
    print("\n--- Deciphered Text ---")
    print(deciphered_text)
    
    
    

def letter_count(text):
    """Count how many times each letter appears in the text. """
    letter_dictionary = {}
    
    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            
            if ch in letter_dictionary:
                letter_dictionary[ch] += 1
            else:
                letter_dictionary[ch] = 1
    return letter_dictionary
    

def caesar_cipher(text, shift):
    """Shift each letter in the text by the given number of positions."""

    # The modulo keeps the position between 0 and 25
    result = ""

    for char in text:
        if 'A' <= char <= 'Z':
            # Shift uppercase letters
            new_pos = (ord(char) - ord('A') + shift) % 26
            result += chr(ord('A') + new_pos)

        elif 'a' <= char <= 'z':
            # Shift lowercase letters
            new_pos = (ord(char) - ord('a') + shift) % 26
            result += chr(ord('a') + new_pos)

        else:
            # Leave non-letters unchanged
            result += char

    return result


if __name__ == "__main__":
    main()