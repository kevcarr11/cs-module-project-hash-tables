# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
def load_cipher():
    text_file = open("ciphertext.txt", "r")
    cipher = text_file.read()
    text_file.close()
    return cipher

def analyze_text(text):
    count = 0
    letter_count = 0
    for char in text:
        if char.isalpha():
            count += 1
    for i in text:
        







letter_frequency = {
    'E': 11.53,
    'T': 9.75,
    'A': 8.46,
    'O': 8.08,
    'H': 7.71,
    'N': 6.73,
    'R': 6.29,
    'I': 5.84,
    'S': 5.56,
    'D': 4.76,
    'L': 3.92,
    'W': 3.08,
    'U': 2.59,
    'G': 2.48,
    'F': 2.42,
    'B': 2.19,
    'M': 2.18,
    'Y': 2.02,
    'C': 1.58,
    'P': 1.08,
    'K': 0.84,
    'V': 0.59,
    'Q': 0.17,
    'J': 0.07,
    'X': 0.07,
    'Z': 0.03
}




# encode_table = {
#     'A': 'H',
#     'B': 'Z',
#     'C': 'Y',
#     'D': 'W',
#     'E': 'O',
#     'F': 'R',
#     'G': 'J',
#     'H': 'D',
#     'I': 'P',
#     'J': 'T',
#     'K': 'I',
#     'L': 'G',
#     'M': 'L',
#     'N': 'C',
#     'O': 'E',
#     'P': 'X',
#     'Q': 'K',
#     'R': 'U',
#     'S': 'N',
#     'T': 'F',
#     'U': 'A',
#     'V': 'M',
#     'W': 'B',
#     'X': 'Q',
#     'Y': 'V',
#     'Z': 'S'
# }

# decode_table = {}

# for key, value in encode_table.items():
#     decode_table[value] = key

# def encode(plain_text):
#     cipher = ''

#     for char in plain_text:
#         if char.isspace():
#             cipher += ' '
#         else:
#             cipher += encode_table[char.upper()]

#     return cipher


# def decode(cipher_text):
#     plain_text = ''
#     for char in cipher_text:
#         if char.isspace():
#             plain_text += ' '
#         else:
#             plain_text += decode_table[char]

#     return plain_text



# print(decode('LV CHLO PN IOMPC').lower())