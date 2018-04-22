import string


def main():
    # Шифрование
    mode = input('Choice mode [E]ncrypt/[D]ecrypt: ')
    if mode.upper() != 'D':
        text = ''.join([i for i in input('Write text: ').lower() if i in string.ascii_lowercase+' '])
        keys = {
            'a': '!', 'b': '@', 'c': '#',
            'd': '$', 'e': '%', 'f': '^',
            'g': '&', 'h': '*', 'i': '(',
            'j': ')', 'k': '-', 'l': '=',
            'm': '+', 'n': '?', 'o': ':',
            'p': ';', 'q': '<', 'r': '>',
            's': '/', 't': '[', 'u': ']',
            'v': '{', 'w': '}', 'x': '|',
            'y': '.', 'z': ',', ' ': '~'
        }
        crypt = ""
        for i in text:
            if i in keys:
                crypt += keys[i]
        print("Crypted text:\n" + crypt + "\n")
    else:
        # Расшифрование

        keys = {
            '!': 'a', '@': 'b', '#': 'c',
            '$': 'd', '%': 'e', '^': 'f',
            '&': 'g', '*': 'h', '(': 'i',
            ')': 'j', '-': 'k', '=': 'l',
            '+': 'm', '?': 'n', ':': 'o',
            ';': 'p', '<': 'q', '>': 'r',
            '/': 's', '[': 't', ']': 'u',
            '{': 'v', '}': 'w', '|': 'x',
            '.': 'y', ',': 'z', '~': ' '
        }
        text = ''.join([i for i in input('Write encrypted text: ') if i in list(keys.keys())])
        decrypt = ""
        for i in text:
            if i in keys:
                decrypt += keys[i]
        print("Decrypted text:\n" + decrypt)
