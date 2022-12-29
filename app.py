from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fill-survey", methods=['POST'])
def survey():
    from panda import inputSurveyCode, FillOutSurvey
    code = "1111 1111 1111 1111 22"
    email_addr = 'eee@gmail.com'
    lastDigits = code[len(code)-2:len(code):]
    code = code[:len(code)-2:]
    inputSurveyCode(code, lastDigits)
    FillOutSurvey(email_addr)

if __name__ == '__main__':
    app.run(debug=True)