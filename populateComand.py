# populate_db.py
import random
import sqlite3
from datetime import datetime, timedelta

def create_table():
    conn = sqlite3.connect('user_habits.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE habits (id INTEGER PRIMARY KEY, user_id INTEGER, habit TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

def insert_habit(user_id, habit, timestamp):
    conn = sqlite3.connect('user_habits.db')
    c = conn.cursor()
    c.execute("INSERT INTO habits (user_id, habit, timestamp) VALUES (?, ?, ?)", (user_id, habit, timestamp))
    conn.commit()
    conn.close()

def generate_random_habits(num_habits):
    users = [1, 2, 3]
    habits = ['Went for a run', 'Ate a salad', 'Meditated for 20 minutes']
    timestamps = [(datetime.now() - timedelta(minutes=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M:%S') for _ in range(num_habits)]

    for i in range(num_habits):
        insert_habit(random.choice(users), random.choice(habits), timestamps[i])

if __name__ == '__main__':
    create_table()
    generate_random_habits(100)