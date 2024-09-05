from flask import Flask, render_template
from random import randrange

app = Flask(__name__)

fonts = [
    "Tangerine",
    "Rancho",
    '"Nerko One", cursive',
    '"Sevillana", cursive',
    '"Anton", sans-serif',
    '"Acme", sans-serif',
    '"Rowdies", sans-serif',
    '"Alfa Slab One", serif',
    '"Spicy Rice", serif;',
]
fonts = [
    fonts[randrange(0, len(fonts), 1)],
    fonts[randrange(0, len(fonts), 1)],
    fonts[randrange(0, len(fonts), 1)],
    fonts[randrange(0, len(fonts), 1)],
]
font_size = [
    randrange(70, 80, 1),
    randrange(50, 60, 1),
    randrange(55, 75, 1),
    randrange(55, 65, 1),
    randrange(50, 90, 1),
    randrange(30, 45, 1),
]

colors = ["red", "orange", "tan", "fuchsia", "navy", "teal", "olive", "green", "black"]
colors = [
    colors[randrange(0, len(colors), 1)],
    colors[randrange(0, len(colors), 1)],
    colors[randrange(0, len(colors), 1)],
    colors[randrange(0, len(colors), 1)],
    colors[randrange(0, len(colors), 1)],
    colors[randrange(0, len(colors), 1)],
    colors[randrange(0, len(colors), 1)],
    colors[randrange(0, len(colors), 1)],
    colors[randrange(0, len(colors), 1)],
]


@app.route("/<string:letter>/")
def letras(letter):
    minus_letter = letter.lower()
    mayus_letter = letter.upper()

    return render_template(
        "index.html",
        minus_letter=minus_letter,
        mayus_letter=mayus_letter,
        fonts=fonts,
        font_size=font_size,
        colors=colors,
    )
