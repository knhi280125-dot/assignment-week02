from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(_name_)

@app.route("/")
def index():
    return "歡迎進入玩慶兒的網頁!"

@app.route("/today")
def today():
    # Giờ Đài Loan
    tz = pytz.timezone("Asia/Taipei")
    now = datetime.now(tz)
    
    # Truyền datetime sang html
    return render_template("today.html", datetime=now)

if _name_ == "_main_":
    app.run(debug=True)
