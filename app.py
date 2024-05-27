from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Add configuration for using SqLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

# Models
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    
    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}"

# Define a route for the root URL
@app.route('/')
def index():
    profiles = Profile.query.all()
    return render_template('index.html', profiles=profiles)

# Function to add profiles
#route/method/define fun/request/validate/create object/add redirect
@app.route('/add',methods=['POST'])
def add_profile():
    first_name=request.form.get('first_name')
    last_name=request.form.get('last_name')
    age=request.form.get('age')
    if first_name!=""and last_name!=""and age is not None:
        profile=Profile(first_name=first_name,last_name=last_name,age=age)
        db.session.add(profile)
        db.session.commit()
    return redirect('/')
#delete
@app.route('/delete/<int:id>')
def delete_profile(id):
    profile=Profile.query.get(id)
    if profile:
        db.session.delete(profile)
        db.session.commit()
    return redirect('/')


#set up shell
def make_shell_context():
    return {'app':app,'db':db,'Profile':Profile}
app.shell_context_processor(make_shell_context)


if __name__ == '__main__':
    app.run(debug=True)