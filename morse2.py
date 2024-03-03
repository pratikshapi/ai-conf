# Morse code dictionary
morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}

# Your encoded Morse code like string
encoded_string = "MOMM TOMO0TTMEMTMTTTTTTA OT TTMTT TOTMTMMM0 TTTOOOT0OMTMMTMTMNTMTO T     T  TTTT T TTT TT OT TT W TT 0MMTTO OM E T M TOT T  N TMMM MT  TT OT T  MT OM  MTT TTM M"

# Replace "M" with "-", "T" with ".", and "0" with " " (space)
morse_code = encoded_string.replace('M', '-').replace('T', '.').replace('0', ' ').replace('A', '').replace('W', '').replace('E', '').replace('N', '')

# Split the string into Morse code words
morse_words = morse_code.split('  ')

# Decode each Morse code word
decoded_words = []
for word in morse_words:
    # Split word into individual Morse code characters
    morse_chars = word.split()
    # Decode each Morse code character
    decoded_chars = [morse_dict.get(char, '') for char in morse_chars]
    # Combine decoded characters into a word
    decoded_word = ''.join(decoded_chars)
    # Add the decoded word to the list of decoded words
    decoded_words.append(decoded_word)

# Combine decoded words into a message
decoded_message = ' '.join(decoded_words)

print(decoded_message)
