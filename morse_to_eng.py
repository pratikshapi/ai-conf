morse_code = "-- ----  ---  -- .-  -..----   -  -.- -- --.- .----  --- --- . ---- -- . -- -  - - - - -.-----  - .- - ----------  -   - ----  ------ - -- ---   - .-- .-----.-----.---- . .-  - .- ---.-------.--.---- .. -- ----.  ------..---.-   - - - -.--.- --- -.- ---. ---- -.--.  --.--- --- - .---- ---  -- -  -- -- -  --  -  -. -.  - .- - ---    -     -        ----  ----  - --       - ---  -   -    - - - -  -  .-  --- -  -- --   .-- - -  -     ---.-  -- -- -  - ---   ---- ---   .     -   --     -  ---- -  ------  --      -.    - -- ------- -- - -. -      - -    --- -    -        -- .-- ---  -- - --  -. - -     - -  .-   --   "
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', 
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-', ' ': ' '
}

# Normalize the Morse code by ensuring consistent spaces for word separation
normalized_morse_code = '   '.join([' '.join(word.split()) for word in morse_code.split('   ')])

def morse_to_text(code, code_dict):
    english_text = ''
    words = code.strip().split('   ')  # Split the morse code into words
    for word in words:
        letters = word.split(' ')  # Split the word into letters
        for letter in letters:
            english_text += code_dict.get(letter, '')  # Convert each letter and add to the text
        english_text += ' '  # Add space after each word
    return english_text.strip()

# Decode the Morse code to English
english_text = morse_to_text(normalized_morse_code, morse_code_dict)
print(english_text)
