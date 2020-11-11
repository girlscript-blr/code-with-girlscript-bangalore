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

class Schedule(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    home_team=db.Column(db.Text,nullable=False)
    away_team=db.Column(db.Text,nullable=False)
    venue=db.Column(db.Text,nullable=False)

    def __repr__(self):
        return 'schedule '+str(self.id)

def get_schedule():
    all_data=Teams.query.all()
    temp=Schedule.query.all()
    if len(temp)==0:
        for i in all_data:
            for j in all_data:
                if i.id==j.id:
                    continue
                else:
                    sch=Schedule(home_team=i.name,away_team=j.name,venue=i.home_ground)
                    db.session.add(sch)
                    db.session.commit()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        all_teams=Teams.query.all()
        if len(all_teams)!=0 :
            db.session.query(Teams).delete()
            db.session.query(Schedule).delete()
            db.session.commit()
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

        flash("*Add remaining teams")
        return render_template('addteams.html')

    return render_template('addteams.html')

@app.route('/display')
def display():
    all_teams=Teams.query.all()
    if len(all_teams)==0:
        flash("*ERROR!No registered team found!")
        return redirect(url_for('index'))
    return render_template('display.html',teams=all_teams,x=teams)

@app.route('/delete')
def delete():
    all_teams=Teams.query.all()
    if len(all_teams)==0 :
        flash("*ERROR!0 item to delete!")
        return redirect(url_for('index'))
    db.session.query(Teams).delete()
    db.session.query(Schedule).delete()
    db.session.commit()
    flash("*ALL Data deleted!")
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    get_schedule()
    sch=Schedule.query.all()
    if len(sch)==0:
        flash("Error!0 teams have registered, please register teams. ")
        return render_template('index.html')
    else:
        tot=teams*(teams-1)
        return render_template('schedule.html',schedule=sch,total=tot)


if __name__=="__main__":
    app.run(debug=True)
