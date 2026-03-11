from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tel = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Create the table
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    leaderboard = Attempt.query.order_by(Attempt.date.desc()).all()
    return render_template('index.html', leaderboard=leaderboard)

@app.route('/admin')
def admin():
    leaderboard = Attempt.query.order_by(Attempt.date.desc()).all()
    return render_template('admin.html', leaderboard=leaderboard)

@app.route('/start', methods=['POST'])
def start():
    subj = request.form.get('subj')  # e.g., 'subj2'
    time = request.form.get('time')

    subjects = {
        'subj1': 'Chemistry',
        'subj2': 'Physics',
        'subj3': 'Economics',
        'subj4': 'Government',
        'subj5': 'Mathematics',
        'subj6': 'English',
        'subj7': 'Commerce',
        'subj8': 'Accounting',
        'subj9': 'Lit-In-English'
    }

    if subj in subjects:
        return redirect(url_for(subj, time=time, subj_name=subjects[subj]))
    return "Invalid selection."

@app.route('/subj1')
def subj1():
    return render_template('subj1.html')

@app.route('/subj2')
def subj2():
    return render_template('subj2.html')

@app.route('/subj3')
def subj3():
    return render_template('subj3.html')

@app.route('/subj4')
def subj4():
    return render_template('subj4.html')

@app.route('/subj5')
def subj5():
    return render_template('subj5.html')

@app.route('/subj6')
def subj6():
    return render_template('subj6.html')

@app.route('/subj7')
def subj7():
    return render_template('subj7.html')

@app.route('/subj8')
def subj8():
    return render_template('subj8.html')

@app.route('/subj9')
def subj9():
    return render_template('subj9.html')

# API endpoint to save attempt after quiz ends
@app.route('/save_attempt', methods=['POST'])
def save_attempt():
    data = request.json
    name = data.get('name')
    tel = data.get('tel')
    subject = data.get('subject')
    score = data.get('score')
    total = data.get('total')

    attempt = Attempt(name=name, tel=tel, subject=subject, score=score, total=total)
    db.session.add(attempt)
    db.session.commit()
    return {"status": "success"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
