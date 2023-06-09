# Morse encoder and decoder
Morse code encoder and decoder website built with Python and Flask. Encodes latin-script text to morse code and decodes morse code to latin-script. Plays the morse code audio when encoding.

## Getting started
1. Clone the repository:
```
git clone https://github.com/while-is-alex/morse-encoder-decoder.git
```

2. Change the directory to the project folder.

3. Create a virtual environment:
```
py -m venv venv
venv/Scripts/activate
```

4. Install the required packages:
```
pip install -r requirements.txt
```

5. Finally, to get the website running, run the `main.py` file. The website will launch and display the home screen.

## Features
### Encoding
This website takes a latin-script (also known as roman-script) text input from the user and encodes it into morse code.

![home-screen.png](https://i.ibb.co/SJRXqPT/home.png)

### Morse sound
Once a latin-script text has been provided and the user clicks on the "translate" button, the morse code sound will play.

![encoding](https://i.ibb.co/VLyb2Gb/encoding.png)

### Decoding
If, instead of a latin-script text, a morse code text is provided, the website intelligently recognizes that it has to decode from morse now and returns a latin-script text at the result screen.

![decoding](https://i.ibb.co/HPvJswc/decoding.png)

## Requirements
This app requires the following:

+ Python 3
+ Flask
+ Flask-Bootstrap
+ Playsound
