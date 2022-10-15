# from email import message
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

app = Flask(__name__)
app.secret_key = "XXX"

@app.route("/")
def index():
    # if session['status'] == "signin":
    #     return redirect(url_for("signin_sucess"))
    return render_template('index.html', title = '首頁', header = '歡迎光臨，請輸入帳號密碼')


@app.route("/square/<int:num>")
def square_calculation(num):
    result = num * num
    return render_template('calculation.html', title = '結果頁', header = '正整數平方計算結果', square = result)

@app.route("/square")
def square():
    num = request.args.get("num", "")
    if num == "":
        return redirect(url_for("index"))
    return redirect(f"/square/{num}")

@app.route("/signin", methods = ["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == '' or password == '':
        return redirect(url_for("signin_fail", message = "請輸入帳號、密碼"))
    
    if username == 'test' and password == 'test':
        session["status"] = "signin"
        return redirect(url_for("signin_sucess"))
    
    return redirect(url_for("signin_fail", message = "帳號或密碼輸入錯誤"))

@app.route("/member")
def signin_sucess():
    if session['status'] == "signout":
        return redirect(url_for("index"))
    return render_template('member.html', title = '會員頁', header = '歡迎光臨，這是會員頁')

@app.route("/error")
def signin_fail():
    message = request.args.get("message", "")
    return render_template('error.html', title = '失敗頁', header = '失敗頁面', message = message)

@app.route("/signout")
def signout():
    session["status"] = "signout"
    return redirect(url_for("index"))

app.run(port = 3000)