from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    return '歡迎進入玩慶兒的網頁!
<a href="/math">點進去輸入x, opt, y (數學運算)'

@app.route("/mis")
def course():
    return "這是資管系的課程頁面"

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
            elif opt == "/": res = x / y if y != 0 else "Lỗi chia cho 0"
            else: res = "Phép tính không hợp lệ"
            return f"Kết quả: {x} {opt} {y} = {res}

<a href='/math'>Quay lại"
        except:
            return "Vui lòng nhập số hợp lệ!
<a href='/math'>Quay lại"
    return '''
        <form method="post">
            Số x: <input type="number" name="x" step="any" required>


            Phép tính (+, -, *, /): <input type="text" name="opt" required>


            Số y: <input type="number" name="y" step="any" required>


            <button type="submit">計算 (Tính toán)
        </form>
        
<a href="/">Quay về trang chủ
    '''

if __name__ == "__main__":
    app.run(debug=True)
