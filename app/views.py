from os import path
from flask import render_template

from app import app
from app.lib.lorem import Lorem

@app.route("/")

def index():
    print(__file__)
    filepath = path.join(path.dirname(__file__), 
    	"data/lorem.txt")
    
    print(filepath)

    lorem = Lorem(words_file=filepath)

    lorem_text =  str(lorem.words)
    lorem_text = lorem.get_lorem_text(200, 350)

    return render_template("index.html", lorem_text=lorem_text )