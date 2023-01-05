from flask import Flask, render_template, redirect, request, url_for, session
import os
from dotenv import load_dotenv
from threading import Thread

app = Flask(__name__)

load_dotenv()
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def home():
    print("ok")
    session['visited'] = True
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    print(request.form["email"])
    print(request.form["CN1"])
    print(request.form["CN2"])
    print(request.form["CN3"])
    print(request.form["CN4"])
    print(request.form["CN5"])
    print(request.form["CN6"])
    return render_template("index.html")

@app.route("/loading", methods=['POST'])
def loading():
    data = request.get_json()
    print(data['email'])
    session["email"] = data['email']
    print(session["email"] + "eeeeeeeeeeeee")
    session["CN1"] = data['CN1']
    session["CN2"] = data['CN2']
    session["CN3"] = data['CN3']
    session["CN4"] = data['CN4']
    session["CN5"] = data['CN5']
    session["CN6"] = data['CN6']
    return render_template("loading.html")
    from panda import inputSurveyCode, FillOutSurvey
    if "email" in session:
        print(session["email"])
        email =session["email"]
        code = "1111 1111 1111 1111 22"
        lastDigits = code[len(code)-2:len(code):]
        code = code[:len(code)-2:]
        inputSurveyCode(code, lastDigits)
        FillOutSurvey(email)
        return render_template("loading.html")

@app.route("/test")
def test():
    return render_template("loading.html")

@app.route("/complete")
def complete():
    return render_template("complete.html")

@app.route("/invalid")
def invalid():
    return render_template("invalid.html")

@app.route("/fill-survey", methods=['POST'])
def survey():
    from production_panda import inputSurveyCode, FillOutSurvey
    try:
        code = session['CN1'] + " " + session['CN2'] + " " + session['CN3'] + " " + session['CN4'] + " " + session['CN5'] + " " + session['CN6']
        print("code: " +code)
        lastDigits = code[len(code)-2:len(code):]
        code = code[:len(code)-2:]
        inputSurveyCode(code, lastDigits)
        t = Thread(target=FillOutSurvey, args=(session["email"],))
        t.start()
    except Exception as e:
        print(e)
        session.clear()
        return redirect(url_for("invalid"))
    session.clear()
    return redirect(url_for("complete"))

if __name__ == '__main__':
    app.run(host='0.0.0.0')