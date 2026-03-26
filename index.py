from flask import Flask

app = Flask(_name_)

@app.route("/")
def index():
    return "歡迎進入玩慶兒的網頁!"

if _name_ == "_main_":
    app.run(debug=True)
