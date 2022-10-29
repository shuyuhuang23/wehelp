# from email import message
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import mysql.connector
from config import mysqldb

connection = mysql.connector.connect(
    user     = mysqldb.user, 
    password = mysqldb.password,
    host     = mysqldb.host,
    database = mysqldb.database
)

app = Flask(__name__)
app.secret_key = "XXX"

@app.route("/")
def index():
    if session['status'] == "signin":
        return redirect(url_for("signin_success"))
    return render_template('index.html', title = '首頁', header = '歡迎光臨，請註冊登入系統')

@app.route("/signup", methods = ["POST"])
def signup():
    name     = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    if name == '' or username == '' or password == '':
        return redirect(url_for("action_error", message = "請輸入姓名、帳號、密碼"))
    with connection.cursor() as cursor:
        select_db_query = f"SELECT * FROM member WHERE username = '{username}'"
        cursor.execute(select_db_query)
        result = cursor.fetchall()
        if len(result) > 0:
            return redirect(url_for("action_error", message = "帳號已經被註冊"))
        else:
            insert_db_query = f'''
            INSERT INTO member (`name`, username, `password`)
            VALUES 
                ('{name}', '{username}', '{password}')
            '''
            cursor.execute(insert_db_query)
            connection.commit()
            return redirect("/")

@app.route("/signin", methods = ["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == '' or password == '':
        return redirect(url_for("action_error", message = "請輸入帳號、密碼"))
    
    with connection.cursor() as cursor:
        select_db_query = f"SELECT id, name, username, password FROM member WHERE username = '{username}'"
        cursor.execute(select_db_query)
        result = cursor.fetchall()
        if len(result) == 1 and result[0][3] == password:
            session["status"] = "signin"
            session["user_id"] = result[0][0]
            session["name"] = result[0][1]
            return redirect(url_for("signin_success"))
        else:
            return redirect(url_for("action_error", message = "帳號或密碼輸入錯誤"))

@app.route("/member")
def signin_success():
    if session['status'] == "signout":
        return redirect(url_for("index"))
    name = session.get("name")
    with connection.cursor() as cursor:
        select_db_query = f"SELECT b.name, a.content FROM message a JOIN member b on a.member_id = b.id ORDER BY a.time DESC"
        cursor.execute(select_db_query)
        result = cursor.fetchall()
        message = [{'name': item[0], 'content': item[1]} for item in result]

    return render_template('member.html', title = '會員頁', header = '歡迎光臨，這是會員頁', name = name, message = message)

@app.route("/message", methods = ["POST"])
def insert_message():
    content = request.form["content"]
    with connection.cursor() as cursor:
        insert_db_query = f'''
        INSERT INTO `message` (member_id, content)
        VALUES 
            ({session.get('user_id')}, "{content}")
        '''
        cursor.execute(insert_db_query)
        connection.commit()
        return redirect("/member")

@app.route("/error")
def action_error():
    message = request.args.get("message", "")
    return render_template('error.html', title = '失敗頁', header = '失敗頁面', message = message)

@app.route("/signout")
def signout():
    session["status"] = "signout"
    del session["user_id"]
    del session["name"]
    return redirect(url_for("index"))

app.run(port = 3000, debug = True)