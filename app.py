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

@app.route("/fill-survey", methods=['GET','POST'])
def survey():
    if request.method == "GET":
        return "ur moma"
    print(session["email"] + "eeeeeeeeeeeee")
    from production_panda import inputSurveyCode, FillOutSurvey
    code = "1111 2222 3333 4444 5555 22"
    code = session['CN1'] + " " + session['CN2'] + " " + session['CN3'] + " " + session['CN4'] + " " + session['CN5'] + " " + session['CN6']
    #email_addr = request.form["email"]
    lastDigits = code[len(code)-2:len(code):]
    code = code[:len(code)-2:]
    #session["email"] =  email_addr
    print(session["email"])
    # return redirect(url_for("loading"))
    # return render_template("loading.html")
    try:
        inputSurveyCode(code, lastDigits)
        t = Thread(target=FillOutSurvey, args=(session["email"],))
        t.start()
    except:
        return redirect(url_for("invalid"))
    return redirect(url_for("complete"))

if __name__ == '__main__':
    app.run(host='0.0.0.0')