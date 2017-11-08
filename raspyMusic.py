from flask import Flask, render_template
app = Flask(__name__)

@app.route("/raspyMusic")
def raspyMusic():
    return render_template('/main.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug = True)
