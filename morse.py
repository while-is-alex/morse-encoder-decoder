from playsound import playsound
from time import sleep


class MorseCode:
    def __init__(self):
        """Initializes the text to morse dictionary that will be used for translation."""
        self.dictionary = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '?': '..--..',
            '!': '-.-.--',
            '.': '.-.-.-',
            ',': '--..--',
            ';': '-.-.-.',
            ':': '---...',
            '+': '.-.-.',
            '-': '-....-',
            '/': '-..-.',
            '=': '-...-',
            ' ': '/',
        }

    def translate(self, text):
        """Receives a string (text or morse) to be translated and
        passes it through the text to morse dictionary."""
        # Checks if the character in the sentence are latin alphabet or morse code.
        is_latin_script = False
        for character in text:
            if character != '.' and character != '-' and character != ' ' and character != '/':
                if character in self.dictionary.keys():
                    is_latin_script = True

        if is_latin_script:
            morse_text = ''
            for character in text:
                if character in self.dictionary.keys():
                    morse_text += f'{self.dictionary[character]} '
                else:
                    return 'Character or symbol not registered in our database.'
            return morse_text

        else:
            latin_text = ''
            # A morse letter can be composed of a single or multiple symbols, so the code goes through the symbols
            # deciding when each morse letter is finished.
            morse_letter = ''
            for position in range(len(text)):
                symbol = text[position]
                # Checks if it is the end of the sentence. If it is the end of the sentence, none of the conditions
                # that come next will be met.
                if position == len(text) - 1:
                    morse_letter += symbol
                    for key, value in self.dictionary.items():
                        if morse_letter == value:
                            latin_text += key
                    morse_letter = ''

                # Each morse letter is separated by an empty space ' ', so each symbol is added to the string
                # morse_letter until a morse letter is formed (denoted by the empty space) and only then the morse
                # letter is translated.
                if symbol != ' ':
                    morse_letter += symbol
                else:
                    for key, value in self.dictionary.items():
                        if morse_letter == value:
                            latin_text += key
                    # After the morse letter is translated, the morse_letter variable is reset so a new morse letter
                    # can be processed.
                    morse_letter = ''
            return latin_text

    def play(self, morse_code):
        """Receives a morse code (string) and turns it into sound."""
        for signal in morse_code:
            print(signal)
            if signal == '.':
                playsound('static/dit.wav')
                sleep(.05)
            elif signal == '-':
                playsound('static/dah.wav')
                sleep(.05)
            elif signal == '/':
                sleep(.5)
            elif signal == ' ':
                sleep(.05)
