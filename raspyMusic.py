#import os
#import RPi.GPIO as GPIO
from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, TextAreaField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

#GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '5fe584s61fe849fs951f1s6e'


class submitSongForm(Form):
    songTitle = StringField('Song Title:', validators=[DataRequired()])
    url = StringField('URL:', validators=[URL()])

@app.route("/raspyMusic/", methods=['GET','POST'])
def raspyMusic():
    form = submitSongForm(request.form)
    if request.method == 'POST':
        songTitle = request.form['songTitle']
        url = request.form['url']
        print(songTitle)
        print(url)
        if form.validate():
            flash('Thanks for your submission. RPi will begin playback...')
        #if url:
            #os.system('mpg123 -q ' + url + ' &')
    return render_template('submitSong.html', form=form)



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug = True)
