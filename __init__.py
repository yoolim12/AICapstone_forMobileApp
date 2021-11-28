from flask import Flask, redirect, session, request, url_for
from flask_sqlalchemy import SQLAlchemy
from model import Members

app = Flask(__name__)

# database 설정파일

id = 'root'
password = 'yy212089--'
host = '127.0.0.1'
db_name = 'user_db'
port = '3306'

# conn = pymysql.connect(host=host,
#                         user=id,
#                         password=password,
#                         db=db_name,
#                         charset='utf8')
# curs = conn.cursor()

# re_str = 'mysql+mysqlconnector://' + id + ':' + \
# password + '@' + host + '/' + db_name + ''

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + id + ':' + \
password + '@localhost:' + port + '/' + db_name

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = 'super secret key'
userdb = SQLAlchemy(app)

userinfo = []

@app.route("/")
def home():
    # session['logged_in'] = False
    if session.get('logged_in'):
        return redirect(url_for('mainpage'))
        # return "success"
    else:
        return redirect(url_for('login'))
    
@app.route('/login', methods=['GET'])
def login():
    id = request.args.get('id')
    pw = request.args.get('pw')
    
    for data in userdb.session.query(Members).all():
        print("data: ", userdb.session.query(Members).all())
        print("id: ", data.id)
        print("pw: ", data.password)
        print("name: ", data.name)
        if id == data.id and password == data.password:
            session['logged_in'] = True
            return {'message':'success'}
        else:
            # flash("이메일 주소 또는 비밀번호가 올바르지 않습니다.") 
            return {'message':'fail'}
        
@app.route('/register', methods=['POST'])
def register():
    # username을 key, password를 value로 하여 userinfo 리스트에 추가하세요.
    id = request.form['id']
    name = request.form['name']
    password = request.form['password']
    members = Members(id, password, name)
    userdb.session.add(members)
    userdb.session.commit()
    return {'message':'success'}
    

# @app.route('/login', methods = ['GET'])
# def login():
#     content = request.get_json()
#     id = content['id']
#     pw = content['password']
#     # sql = "select * from user_list"
#     # curs.execute(sql)
#     # rows = curs.fetchall()
#     data = {'id':id, 'password':pw}
#     return json.dumps(data)

# if __name__ == "__main__":
#     app.run(host='localhost', port= 5000)
    # app.run()
# app.run(host='0.0.0.0', port= 3306)

# @app.route('/login', methods=)
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     global userinfo

#     if request.method == 'POST':
#         id = request.form['id']
#         password = request.form['password']

    #     for data in userdb.session.query(Members).all():
    #         print("data: ", userdb.session.query(Members).all())
    #         if id == data.id and password == data.password:
    #             print(id, password)
    #             # 비밀번호 검증 후 일치하는 경우 초기 페이지로 이동하세요.
    #             session['logged_in'] = True
    #             # return redirect(url_for('mainpage'))
    #             # return render_template('mainpage.html')
    #             return redirect(url_for('home'))

    #     flash("이메일 주소 또는 비밀번호가 올바르지 않습니다.")
    #     return redirect(url_for('login'))
    # else:
    #     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # username을 key, password를 value로 하여 userinfo 리스트에 추가하세요.
#         id = request.form['id']
#         name = request.form['name']
#         password = request.form['password']
#         password_check = request.form['passwordcheck']

#         if password == password_check:
#             members = Members(id, password, name)
#             userdb.session.add(members)
#             userdb.session.commit()
        
#             return redirect(url_for('login'))
#         else:
#             flash("비밀번호가 일치하지 않습니다.")
#             return redirect(url_for('register'))
#     else:
#         return render_template('registerpage.html')

# @app.route("/mainpage", methods=["GET", "POST"])
# def mainpage():
#     if request.method == 'POST':
#         pass
#     else:
#         return render_template('mainpage.html')

# if __name__ == "__main__":
#     app.run()

if __name__ == "__main__":
    app.run(host='localhost', port= 5000)