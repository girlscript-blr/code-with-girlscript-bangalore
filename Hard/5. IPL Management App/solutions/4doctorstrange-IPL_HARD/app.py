from flask import Flask,render_template, request,redirect,flash,session,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import sqlite3

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///teams.db'
db=SQLAlchemy(app)
app.secret_key="mwxm"
admin_key='ipl@2020'
teams=0
winner=""
matchno=0
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
    team_won=db.Column(db.Text,nullable=False,default="NA")
    result=db.Column(db.Text,nullable=False,default="NA")
    man_ofthe_match=db.Column(db.Text,nullable=False,default="NA")

    def __repr__(self):
        return 'schedule '+str(self.id)

class Points(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    team_name=db.Column(db.Text,nullable=False)
    wins=db.Column(db.Integer,nullable=False,default=0)
    loss=db.Column(db.Integer,nullable=False,default=0)
    points=db.Column(db.Integer,nullable=False,default=0)

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

        pt=Points(team_name=name)
        db.session.add(pt)
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
    global teams
    teams=len(all_teams)
    if len(all_teams)==0:
        flash("*ERROR!No registered team found!")
        return redirect(url_for('index'))
    return render_template('display.html',teams=all_teams,x=len(all_teams))

@app.route('/delete')
def delete():
    all_teams=Teams.query.all()
    if len(all_teams)==0 :
        flash("*ERROR!0 item to delete!")
        return redirect(url_for('index'))
    db.session.query(Teams).delete()
    db.session.query(Schedule).delete()
    db.session.query(Points).delete()
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
        tot=len(Teams.query.all())
        tot=tot*(tot-1)
        return render_template('schedule.html',schedule=sch,total=tot)

@app.route('/update',methods=['POST','GET'])
def update():
    if len(Schedule.query.all())==0:
        flash('NO data to update!')
        return render_template('index.html')

    if request.method=="POST":
        key=request.form['key']
        if key==admin_key:
            flash("Welcome admin!")
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials!')
            return render_template('index.html')

    return render_template("adminkey.html")

@app.route('/admin',methods=['POST','GET'])
def admin():
    if request.method=="POST":
        global matchno
        matchno=int(request.form['id'])
        sch=Schedule.query.filter_by(id=matchno).all()
        teams=[sch[0].home_team,sch[0].away_team]
        return render_template('updatematch.html',sch=sch,teams=teams)
    
    return render_template('admin.html')

@app.route('/updatematch',methods=['POST','GET'])
def updatematch():
    if request.method=='POST':
        win=request.form['team_won']
        result=request.form['result']
        man_ofthe_match=request.form['man_ofthe_match']
        global winner
        winner=win
        u=Schedule.query.get(matchno).team_won=win
        v=Schedule.query.get(matchno).result=result
        p=Schedule.query.get(matchno).man_ofthe_match=man_ofthe_match
        db.session.commit()
        calculate_points()
        
        
        


    flash('Result successfully updated')
    return render_template("index.html")


def calculate_points():
    query=Schedule.query.get(matchno)
    if query.home_team==winner:
        h=Points.query.filter_by(team_name=query.home_team).all()[0]
        h.wins+=1
        h.points+=2
        db.session.commit()

        a=Points.query.filter_by(team_name=query.away_team).all()[0]
        a.loss+=1
        db.session.commit()

    else:
        a=Points.query.filter_by(team_name=query.away_team).all()[0]
        a.wins+=1
        a.points+=2
        db.session.commit()

        h=Points.query.filter_by(team_name=query.home_team).all()[0]
        h.loss+=1
        db.session.commit()

@app.route('/points')
def points():
    points_table=Points.query.order_by(desc(Points.points)).all()
    if len(points_table)==0:
        flash("No data to display,try adding teams!")
        return render_template("index.html")
    return render_template("points.html",points=points_table)


if __name__=="__main__":
    app.run(debug=True)
