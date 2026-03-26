from flask import Flask, render_template, request

from datetime import datetime, timezone, timedelta

app = Flask(__name__)

…

@app.route("/today")

def today():

tz = timezone(timedelta(hours=+8))

now = datetime.now(tz)

return render_template("today.html", datetime = str(now))

…
