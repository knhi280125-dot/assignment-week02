from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    return '歡迎進入玩慶兒的網頁!
<a href="/math">點進去輸入x, opt, y (數學運算)'

@app.route("/today")
def today():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("today.html", datetime = str(now))

@app.route("/math", methods=["GET", "POST"])
def math():
    if request.method == "POST":
        try:
            x = float(request.form.get("x"))
            y = float(request.form.get("y"))
            opt = request.form.get("opt")
            if opt == "+": res = x + y
            elif opt == "-": res = x - y
            elif opt == "*": res = x * y
            elif opt == "/": res = x / y if y != 0 else "Error: Division by 0"
            else: res = "Invalid"
            return f"Kết quả: {res}
<a href='/math'>Back"
        except:
            return "Error!
<a href='/math'>Back"
    return '<form method="post">x:<input name="x"> opt:<input name="opt"> y:<input name="y">Calc</form>'

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
