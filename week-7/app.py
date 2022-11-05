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
    user = mysqldb.user,
    password = mysqldb.password,
    host = mysqldb.host,
    database = mysqldb.database)

app = Flask(__name__)
app.secret_key = "XXX"


@app.route("/")
def index():
    if session.get('status') == "signin":
        return redirect(url_for("signin_success"))
    return render_template('index.html', title = '首頁', header = '歡迎光臨，請註冊登入系統')


@app.route("/signup", methods = ["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    if name == '' or username == '' or password == '':
        return redirect(url_for("action_error", message = "請輸入姓名、帳號、密碼"))
    with connection.cursor() as cursor:
        select_db_query = "SELECT * FROM member WHERE username = %(username)s"
        cursor.execute(select_db_query, {'username': username})
        result = cursor.fetchall()
        if len(result) > 0:
            return redirect(url_for("action_error", message = "帳號已經被註冊"))
        else:
            insert_db_query = '''
            INSERT INTO member (`name`, username, `password`)
            VALUES 
                (%(name)s, %(username)s, %(password)s)
            '''
            cursor.execute(insert_db_query, 
                {
                           'name': name, 
                           'username': username, 
                           'password': password
                })
            connection.commit()
            return redirect("/")


@app.route("/signin", methods = ["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == '' or password == '':
        return redirect(url_for("action_error", message = "請輸入帳號、密碼"))

    with connection.cursor() as cursor:
        select_db_query = "SELECT id, name, username, password FROM member WHERE username = %(username)s"
        cursor.execute(select_db_query, {'username': username})
        result = cursor.fetchall()
        if len(result) == 1 and result[0][3] == password:
            session["status"] = "signin"
            session["user_id"] = result[0][0]
            session["name"] = result[0][1]
            return redirect(url_for("signin_success"))
        else:
            return redirect(url_for("action_error", message = "帳號或密碼輸入錯誤"))


@app.route("/api/member", methods = ['get', 'patch'])
def get_member():
    print(request)
    if request.method == 'GET':
        username = request.args.get('username')
        with connection.cursor() as cursor:
            # (%(user_id)s, %(content)s)
            select_db_query = "SELECT id, name, username FROM member WHERE username = %(username)s"
            cursor.execute(select_db_query, {'username': username})
            result = cursor.fetchall()
            if len(result) == 0:
                return {"data": None}
            else:
                return {"data": {"id": result[0][0],
                                "name": result[0][1],
                                "username": result[0][2]
                                }}
    
    if request.method == 'PATCH':
        if session.get('status') == "signin":
            with connection.cursor() as cursor:
                update_db_query = '''
                UPDATE member 
                SET 
                    `name` = %(name)s
                WHERE
                    id = %(user_id)s; 
                '''
                cursor.execute(update_db_query, {
                    'user_id': session.get('user_id'), 'name': request.json.get('name')})
                connection.commit()
            session['name'] = request.json.get('name')
            return {"ok": True}
        return {"error": True}

@app.route("/member")
def signin_success():
    if session.get('status') != "signin":
        return redirect(url_for("index"))
    name = session.get("name")
    with connection.cursor() as cursor:
        select_db_query = "SELECT b.name, a.content FROM message a JOIN member b on a.member_id = b.id ORDER BY a.time DESC"
        cursor.execute(select_db_query)
        result = cursor.fetchall()
        message = [{'name': item[0], 'content': item[1]} for item in result]

    return render_template('member.html', title = '會員頁', header = '歡迎光臨，這是會員頁', name = name, message = message)


@app.route("/message", methods=["POST"])
def insert_message():
    content = request.form["content"]
    with connection.cursor() as cursor:
        insert_db_query = '''
        INSERT INTO `message` (member_id, content)
        VALUES 
            (%(user_id)s, %(content)s)
        '''
        cursor.execute(insert_db_query, {
                       'user_id': session.get('user_id'), 'content': content})
        connection.commit()
        return redirect("/member")


@app.route("/error")
def action_error():
    message = request.args.get("message", "")
    return render_template('error.html', title='失敗頁', header='失敗頁面', message=message)


@app.route("/signout")
def signout():
    session["status"] = "signout"
    del session["user_id"]
    del session["name"]
    return redirect(url_for("index"))


app.run(port=3000, debug=True)
