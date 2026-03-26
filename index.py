from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "歡迎進入阮慶兒的網頁!"

@app.route("/mis")
def course():
    return "這是資管系的課程頁面"

@app.route("/today")
def today():
    now = datetime.now().strftime("%Y/%m/%d")
    return render_template("today.html", datetime=now)

if __name__ == "__main__":
    app.run(debug=True)
