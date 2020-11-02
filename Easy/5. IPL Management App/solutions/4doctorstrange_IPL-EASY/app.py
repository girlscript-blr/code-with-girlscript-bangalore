from flask import Flask,render_template, request,redirect,flash,session,url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///teams.db'
db=SQLAlchemy(app)
app.secret_key="mwxm"
teams=0
class Teams(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text,nullable=False)
    captain=db.Column(db.Text,nullable=False)
    franchise=db.Column(db.Text,nullable=False)
    home_ground=db.Column(db.Text,nullable=False)

    def __repr__(self):
        return 'team ' +str(self.id)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['GET','POST'])
def register():
    all_teams=Teams.query.all() 
    if request.method=='POST':
        global teams
        teams=int(request.form['registeration'])
        flash('*Fill the given form to register a team!')
        return redirect(url_for('addteams'))

    return render_template('register.html')

@app.route('/addteams',methods=['POST','GET'])
def addteams():
    if request.method=='POST':
        name=request.form['name']
        captain=request.form['captain']
        franchise=request.form['franchise']
        hg=request.form['home_ground']
        new_team=Teams(name=name,captain=captain,franchise=franchise,home_ground=hg)
        db.session.add(new_team)
        db.session.commit()
        if len(Teams.query.all())==teams:
            flash("*All the teams are added successfully!")
            return render_template('index.html',teams=teams)

        flash("*Enter details of remaining team/teams")
        return render_template('addteams.html')

    return render_template('addteams.html')

@app.route('/display')
def display():
    all_teams=Teams.query.all()
    if len(all_teams)==0:
        flash("*ERROR, no registered team found!")
        return redirect(url_for('index'))
    return render_template('display.html',teams=all_teams,x=teams)

@app.route('/delete')
def delete():
    all_teams=Teams.query.all()
    if len(all_teams)==0:
        flash("*ERROR,0 item to delete!")
        return redirect(url_for('index'))
    db.session.query(Teams).delete()
    db.session.commit()
    flash("*ALL Data deleted!")
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
