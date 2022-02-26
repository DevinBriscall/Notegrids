from flask import Flask, flash, jsonify, redirect, render_template, request, session
import random

app = Flask(__name__)

order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
sharplist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A#', 'C#', 'D#', 'F#','G#']
flatlist = ['A', 'B', 'C', 'D', 'E','F','G', 'Ab', 'Bb', 'Db', 'Eb', 'Gb']
gotten = 1

@app.route("/", methods=["GET", "POST"])
def index():
    global lastlist
    global relevantlist
    gotten = 1
    global order
    # when rendering the page for the first time
    if request.method == "GET":
        order = [0, 7, 1, 2, 8, 3, 9, 4, 5, 10, 6, 11]
        relevantlist = sharplist
        lastlist = sharplist
        return render_template('index.html', order=order, relevantlist=relevantlist)

    # when request method is post
    # make sure form option is selected
    else:

        if not request.form.get('sharpsflats') and gotten == 0:
            print ('no option selected')
            error = "please select option"
            return render_template('index.html', order=order, relevantlist=relevantlist, error=error)
        
        if not request.form.get('sharpsflats') and gotten == 1:
            print ('no option selected')
            random.shuffle(order)
            error = ""
            return render_template('index.html', order=order, relevantlist=relevantlist, error=error)
        if request.form.get('sharpsflats'):
            error = ''
            gotten = 1;
            random.shuffle(order)
            selected = request.form.get("sharpsflats")
            if selected == "sharps":
                relevantlist = sharplist
                lastlist = sharplist
                return render_template('index.html', order=order, relevantlist=relevantlist, error=error)
            else:
                relevantlist = flatlist
                lastliit = flatlist
                return render_template('index.html', order=order, relevantlist=relevantlist, error=error)
        
        return render_template('index.html', order=order, relevantlist=relevantlist, error=error)



