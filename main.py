from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from morse import MorseCode
from forms import MorseForm
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.app_context().push()
load_dotenv()
# app.config['SECRET_KEY'] can be any key, and it will work
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap(app)


@app.route("/")
def home():
    form = MorseForm()
    return render_template("index.html", form=form)


@app.route("/translation", methods=["POST"])
def translation():
    morse = MorseCode()
    form = MorseForm()
    if request.method == "POST":
        text = form.text.data
        translated_text = morse.translate(text.lower())
        morse.play(translated_text)
        return render_template("translation-page.html", translated_text=translated_text)


if __name__ == '__main__':
    app.run(debug=True)
