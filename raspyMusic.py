#import os
#import RPi.GPIO as GPIO
from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, TextAreaField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

#GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '5fe584s61fe849fs951f1s6e'
q = []

# creating the form for song submission
class submitSongForm(Form):
    songTitle = StringField('Song Title:', validators=[DataRequired()])
    url = StringField('URL:', validators=[URL()])

# response to form submission
@app.route("/raspyMusic/", methods=['GET','POST'])
def raspyMusic():
    form = submitSongForm(request.form)
    if request.method == 'POST':
        songTitle = request.form['songTitle']
        url = request.form['url']
        # validate that data is correct
        if form.validate() and url[-4:] == '.mp3':
            flash('Thanks for your submission. RaspyMusic will begin playback...')
            # Append URL to the queue of songs
            q.append(url)
        else :
            flash('ERROR: please try again')
        # if the queue of songs is not empty
        if len(q) != 0:
            # play the song on Raspberry Pi
            #os.system('mpg123 -q ' + q[0] + ' &')
            q.pop(0)

    return render_template('submitSong.html', form=form)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug = True)
