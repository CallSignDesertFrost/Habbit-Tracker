# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_habits.db'
db = SQLAlchemy(app)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    habit = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

@app.route('/track_habit', methods=['POST'])
def track_habit():
    data = request.get_json()
    habit = Habit(user_id=data['user_id'], habit=data['habit'], timestamp=data['timestamp'])
    db.session.add(habit)
    db.session.commit()
    return jsonify({'message': 'Habit tracked'})

if __name__ == '__main__':
    app.run(debug=True)
    