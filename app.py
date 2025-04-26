from flask import Flask , redirect , url_for , render_template , flash , request , session , jsonify
from flask_wtf import FlaskForm
from wtforms import StringField , IntegerField , PasswordField , EmailField , SubmitField , TextAreaField
from wtforms.validators import DataRequired , Email
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin , LoginManager , login_user , current_user , login_required , logout_user , UserMixin
import json
from questions import*

app = Flask(__name__)
app.config["SECRET_KEY"] = "@VCS72xppdv"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = True
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return mydatabase.query.get(int(user_id))
class mydatabase(db.Model , UserMixin):
    id = db.Column(db.Integer ,primary_key = True )
    Name = db.Column(db.String(120) , unique  = False , index = True)
    Course = db.Column(db.String(120) , unique = False , index = True)
    Year = db.Column(db.Integer , unique = False, index= True)
    Email = db.Column(db.String(120) , unique = True , index = True)
    Password = db.Column(db.String(20) , unique = False , index = True)

class signin_form_data(FlaskForm):
    name = StringField("Name" , validators=[DataRequired()])
    course = StringField("Course", validators=[ DataRequired()])
    year = IntegerField("Year" , validators=[DataRequired()])
    email = EmailField("Student Email" , validators=[DataRequired() , Email()])
    password = PasswordField("Password" , validators=[DataRequired()])
    submit = SubmitField("Sign Up")

class login_form_data(FlaskForm):
    email = EmailField("Email" , validators=[DataRequired() , Email()])
    password = PasswordField("Pass" , validators=[DataRequired()])
    submit = SubmitField("Sign In")


@app.route('/' , methods = ['GET' , 'POST'])
def home():
    return render_template("hom.html")

@app.route("/Signin" , methods = ["GET" , "POST"])
def Signin():
    if current_user.is_authenticated:
        return redirect('home')
    signin_form = signin_form_data()
    if signin_form.validate_on_submit():
        email_check = mydatabase.query.filter_by(Email = request.form['email']).first()
        if email_check:
            flash("Sorry!! , This Email already exist" , 'Success')
        else:
            db.session.add(mydatabase(Name = request.form['name'] , Course = request.form['course'] , Year = request.form['year'] , Email = request.form['email'] , Password = request.form["password"]))
            db.session.commit()
            flash("Account Created , You can login now" , 'Success')
            return redirect("login")
    return render_template('sign.html' , template_form = signin_form)

@app.route("/login" , methods = ["GET" , "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("home")
    login_form = login_form_data()
    if login_form.validate_on_submit():
        user = mydatabase.query.filter_by(Email = request.form["email"] , Password = request.form["password"]).first()
        if user:
            login_user(user)
            session['username'] = user.Name
            return redirect("home")
        else:
            flash("Please check your Email or Password" , "Success")
    return render_template("log.html", template_form = login_form)

@app.route("/account")
@login_required
def account():
    return render_template('account.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('login')



@app.route("/learn")
@login_required
def learn():
    return render_template("learn.html")

@app.route("/practice")
@login_required
def practice():
    return render_template('practice.html')

##blcok game for maths and logic
@app.route('/codebuilder')
def codebuilder():
    return render_template('codebuilder.html')

@app.route("/learnpythongame")
def learnpythongame():
    return render_template("learnpythongame.html")

@app.route("/track")
def track():
    return render_template("Track.html")



@app.route('/test/<data>', methods=['POST' , 'GET'])
def test(data):
    global questions
    if data == "Computer Fundamental1":
        questions = Computer_Fundamental1
    elif data == 'Computer Fundamental2':
        questions = Computer_Fundamental2
    elif data == 'Computer Fundamental3':
        questions = Computer_Fundamental3
    elif data == 'Computer Fundamental4':
        questions = Computer_Fundamental4
    elif data == 'Computer Fundamental5':
        questions = 'Computer_Fundamental5'
    elif data == 'C Programming1':
        questions = C_Programming1
    elif data == 'C Programming2':
        questions = C_Programming2
    elif data == 'C Programming3':
        questions = C_Programming3
    elif data == 'C Programming4':
        questions = C_Programming4
    elif data == 'C Programming5':
        questions = C_Programming5 
    elif data == 'Mathematics -I1':
        questions = MathematicsI1
    elif data == 'Mathematics -I2':
        questions = MathematicsI2
    elif data == 'Mathematics -I3':
        questions = MathematicsI3
    elif data == 'Mathematics -I4':
        questions = MathematicsI4
    elif data == 'Mathematics -I5':
        questions = MathematicsI5
    elif data == 'Business Communication1':
        questions = Business_Communication1
    elif data == 'Business Communication3':
        questions = Business_Communication3
    elif data == 'Business Communication4':
        questions = Business_Communication4
    elif data == 'Business Communication5':
        questions = Business_Communication5
    elif data == 'Financial Accounting Management1':
        questions = Financial_Accounting_Management1
    elif data == 'Financial Accounting Management2':
        questions = Financial_Accounting_Management2
    elif data == 'Financial Accounting Management3':
        questions = Financial_Accounting_Management3
    elif data == 'Financial Accounting Management4':
        questions = Financial_Accounting_Management4
    elif data == 'Financial Accounting Management5':
        questions = Financial_Accounting_Management1
    elif data == 'OOP Using C++1':
        questions = C1
    elif data == 'OOP Using C++2':
        questions = C2
    elif data == 'OOP Using C++3':
        questions = C3
    elif data == 'OOP Using C++4':
        questions = C4
    elif data == 'OOP Using C++5':
        questions = C5
    elif data == 'Organization Behavior1':
        questions = OB1
    elif data == 'Organization Behavior2':
        questions = OB2
    elif data == 'Organization Behavior3':
        questions = OB3
    elif data == 'Organization Behavior4':
        questions = OB4
    elif data == 'Organization Behavior5':
        questions = OB5
    elif data == 'Organization Behavior6':
        questions = OB6
    elif data == 'Mathematics -II1':
        questions = MII1
    elif data == 'Mathematics -II2':
        questions = MII2
    elif data == 'Mathematics -II3':
        questions = MII3
    elif data == 'Mathematics -II4':
        questions = MII4
    elif data == 'Mathematics -II5':
        questions = MII5
    elif data == 'Python1':
        questions = py1
    elif data == 'Python2':
        questions = py2
    elif data == 'Python3':
        questions = py3
    elif data == 'Python4':
        questions = py4
    elif data == 'Python5':
        questions = py5
    elif data == 'Data Structure Using C & C++1':
        questions = dsa1
    elif data == 'Data Structure Using C & C++2':
        questions = dsa2
    elif data == 'Data Structure Using C & C++3':
        questions = dsa3
    elif data == 'Data Structure Using C & C++4':
        questions = dsa4
    elif data == 'Data Structure Using C & C++5':
        questions = dsa5
    elif data == 'Elements of Statistics1':
        questions = Elements_of_Statistics1
    elif data == 'Elements of Statistics2':
        questions = Elements_of_Statistics2
    elif data == 'Elements of Statistics3':
        questions = Elements_of_Statistics3
    elif data == 'Elements of Statistics4':
        questions = Elements_of_Statistics4
    elif data == 'Elements of Statistics5':
        questions = Elements_of_Statistics5
    elif data == 'Computer Graphics & Animation1':
        questions = graphic1
    elif data == 'Computer Graphics & Animation2':
        questions = graphic2
    elif data == 'Computer Graphics & Animation3':
        questions = graphic3
    elif data == 'Computer Graphics & Animation4':
        questions = graphic4
    elif data == 'Computer Graphics & Animation5':
        questions = graphic5
    elif data == 'Software Engineering1':
        questions = se1
    elif data == 'Software Engineering2':
        questions = se2
    elif data == 'Software Engineering3':
        questions = se3
    elif data == 'Software Engineering4':
        questions = se4
    else:
        questions = questions

    
    return render_template('test.html', questions=questions , data = data)


##result route

wrong_questions = {}


def initialize_session():
    if 'wrong_questions' not in session:
        session['wrong_questions'] = {}




@app.route('/submit/<data>', methods=['POST' , 'GET'])
def submit(data):
    initialize_session()
    session['wrong_questions'].clear()

    if data == "Computer Fundamental1":
        questions = Computer_Fundamental1
    elif data == 'Computer Fundamental2':
        questions = Computer_Fundamental2
    elif data == 'Computer Fundamental3':
        questions = Computer_Fundamental3
    elif data == 'Computer Fundamental4':
        questions = Computer_Fundamental4
    elif data == 'Computer Fundamental5':
        questions = Computer_Fundamental5
    elif data == 'C Programming1':
        questions = C_Programming1
    elif data == 'C Programming2':
        questions = C_Programming2
    elif data == 'C Programming3':
        questions = C_Programming3
    elif data == 'C Programming4':
        questions = C_Programming4
    elif data == 'C Programming5':
        questions = C_Programming5
    elif data == 'Mathematics -I1':
        questions = MathematicsI1
    elif data == 'Mathematics -I2':
        questions = MathematicsI2
    elif data == 'Mathematics -I3':
        questions = MathematicsI3
    elif data == 'Mathematics -I4':
        questions = MathematicsI4
    elif data == 'Mathematics -I5':
        questions = MathematicsI5  
    elif data == 'Business Communication1':
        questions = Business_Communication1
    elif data == 'Business Communication3':
        questions = Business_Communication3
    elif data == 'Business Communication4':
        questions = Business_Communication4
    elif data == 'Business Communication5':
        questions = Business_Communication5
    elif data == 'Financial Accounting Management1':
        questions = Financial_Accounting_Management1
    elif data == 'Financial Accounting Management2':
        questions = Financial_Accounting_Management2
    elif data == 'Financial Accounting Management3':
        questions = Financial_Accounting_Management3
    elif data == 'Financial Accounting Management4':
        questions = Financial_Accounting_Management4
    elif data == 'Financial Accounting Management5':
        questions = Financial_Accounting_Management5
    elif data == 'OOP Using C++1':
        questions = C1
    elif data == 'OOP Using C++2':
        questions = C2
    elif data == 'OOP Using C++3':
        questions = C3
    elif data == 'OOP Using C++4':
        questions = C4
    elif data == 'OOP Using C++5':
        questions = C5
    elif data == 'Organization Behavior1':
        questions = OB1
    elif data == 'Organization Behavior2':
        questions = OB2
    elif data == 'Organization Behavior3':
        questions = OB3
    elif data == 'Organization Behavior4':
        questions = OB4
    elif data == 'Organization Behavior5':
        questions = OB5
    elif data == 'Organization Behavior6':
        questions = OB6
    elif data == 'Mathematics -II1':
        questions = MII1
    elif data == 'Mathematics -II2':
        questions = MII2
    elif data == 'Mathematics -II3':
        questions = MII3
    elif data == 'Mathematics -II4':
        questions = MII4
    elif data == 'Mathematics -II5':
        questions = MII5
    elif data == 'Python1':
        questions = py1
    elif data == 'Python2':
        questions = py2
    elif data == 'Python3':
        questions = py3
    elif data == 'Python4':
        questions = py4
    elif data == 'Python5':
        questions = py5
    elif data == 'Data Structure Using C & C++1':
        questions = dsa1
    elif data == 'Data Structure Using C & C++2':
        questions = dsa2
    elif data == 'Data Structure Using C & C++3':
        questions = dsa3
    elif data == 'Data Structure Using C & C++4':
        questions = dsa4
    elif data == 'Data Structure Using C & C++5':
        questions = dsa5
    elif data == 'Elements of Statistics1':
        questions = Elements_of_Statistics1
    elif data == 'Elements of Statistics2':
        questions = Elements_of_Statistics2
    elif data == 'Elements of Statistics3':
        questions = Elements_of_Statistics3
    elif data == 'Elements of Statistics4':
        questions = Elements_of_Statistics4
    elif data == 'Elements of Statistics5':
        questions = Elements_of_Statistics5
    elif data == 'Computer Graphics & Animation1':
        questions = graphic1
    elif data == 'Computer Graphics & Animation2':
        questions = graphic2
    elif data == 'Computer Graphics & Animation3':
        questions = graphic3
    elif data == 'Computer Graphics & Animation4':
        questions = graphic4
    elif data == 'Computer Graphics & Animation5':
        questions = graphic5
    elif data == 'Software Engineering1':
        questions = se1
    elif data == 'Software Engineering2':
        questions = se2
    elif data == 'Software Engineering3':
        questions = se3
    elif data == 'Software Engineering4':
        questions = se4
    else:
        questions = questions

    
    your_response = []
    total = -1
    total_marks = 0
    score = 0
    for question in questions:
        total +=1
        total_marks +=1
        selected_option = request.form.get(question['question'])
        if selected_option == question['answer']:
            score += 1
        else:
            session['wrong_questions'][questions[total].get('question')]  = questions[total].get('answer')
            your_response.append(request.form.get(question['question']))
    return render_template('result.html', score=score , total_marks = total_marks , wrong_questions = session['wrong_questions']  ,  your_response = your_response)
#practice_chapter name
@app.route('/practice_sub_name')
@login_required
def practice_sub_name():
    return render_template('practice_sub.html')
#chapter name
@app.route('/chapter_name/<id>')
@login_required
def chapter_name(id):
    return render_template('chapter_name.html' , id = id)



with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

