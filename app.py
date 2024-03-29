from flask import Flask, render_template, redirect, request, url_for, session, make_response
import os
from dotenv import load_dotenv
from threading import Thread

from gevent import monkey
monkey.patch_all()

import requests

app = Flask(__name__)

load_dotenv()
app.secret_key = os.environ.get("SECRET_KEY")

@app.route('/')
def index():
    first_visit = request.cookies.get('first_visit') != 'False'
    response = make_response(render_template("index.html", first_visit=first_visit))
    if first_visit:
        response.set_cookie('first_visit', 'False')
    return response

@app.route("/submit", methods=["POST"])
def submit():
    # print(request.form["email"])
    # print(request.form["CN1"])
    # print(request.form["CN2"])
    # print(request.form["CN3"])
    # print(request.form["CN4"])
    # print(request.form["CN5"])
    # print(request.form["CN6"])
    return render_template("index.html")

@app.route("/loading", methods=['POST'])
def loading():
    data = request.get_json()
    # print(data['email'])
    session["email"] = data['email']
    # print(session["email"] + "eeeeeeeeeeeee")
    session["CN1"] = data['CN1']
    session["CN2"] = data['CN2']
    session["CN3"] = data['CN3']
    session["CN4"] = data['CN4']
    session["CN5"] = data['CN5']
    session["CN6"] = data['CN6']
    return render_template("loading.html")
    from panda import inputSurveyCode, FillOutSurvey
    if "email" in session:
        # print(session["email"])
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

@app.route("/stats")
def stats():
    #from db.countData import CountData
    #totalValidCodes = CountData()
    api_url = 'https://api.api-ninjas.com/v1/counter?id=surveys_filled'
    #print(os.environ.get("API_KEY"))
    totalValidCodes = "3000+"
    try:
        response = requests.get(api_url, headers={'X-Api-Key': "Qr+s2e9EKBowf7w3Gc7zyA==TTyjizMXAvbY7wak"})
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()

            # Access values from the JSON
            totalValidCodes = str(json_data['value'])
    except Exception as e:
        pass

    return render_template("stats.html", totalValidCodes=totalValidCodes)

@app.route("/fill-survey", methods=['POST'])
def survey():
    from production_panda import inputSurveyCode, FillOutSurvey, IncrementStatCount
    from db.insertData import InsertData
    try:
        code = session['CN1'] + " " + session['CN2'] + " " + session['CN3'] + " " + session['CN4'] + " " + session['CN5'] + " " + session['CN6']
        full_code = code
        email = session["email"]
        # print("code: " +code)
        lastDigits = code[len(code)-2:len(code):]
        code = code[:len(code)-2:]
        #print("here")
        inputSurveyCode(code, lastDigits)
        #print("here22")
        t = Thread(target=FillOutSurvey, args=(email,))
        #t2 = Thread(target=InsertData, args=(full_code, email))
        t3 = Thread(target=IncrementStatCount(), args=())
        t.start()
        #t2.start()
        t3.start()
    except Exception as e:
        #print(e)
        session.clear()
        return redirect(url_for("invalid"))
    session.clear()
    return redirect(url_for("complete"))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
