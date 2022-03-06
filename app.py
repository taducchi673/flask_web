from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
# Initialize a database
db = SQLAlchemy(app)
# Create db model
class Friends(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	# Create a function to return a string when we add
	def __repr__(self):
		return '<Name %r>' %self.id

@app.route("/index")
def index():
	flash("What's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
    
@app.route("/say_hello")
def sayhello():
	return render_template("say_hello.html")  
@app.route("/blog_sample")
def blog():
	return render_template("blog.html")  
@app.route("/home")
def home():
	return render_template("home.html")
