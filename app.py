from flask import Flask,render_template
import sqlite3
#import datetime
app = Flask(__name__)


@app.route('/')
def index():
    #time=datetime.date.today()
    #return render_template("index.html",var=time)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
