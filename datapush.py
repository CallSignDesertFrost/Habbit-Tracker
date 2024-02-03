# send_to_data_warehouse.py
import psycopg2
import sqlite3

def send_to_data_warehouse(habits):
    conn = psycopg2.connect(
        dbname="data_warehouse",
        user="your_user",
        password="your_password",
        host="your_host",
        port="your_port"
    )

    cur = conn.cursor()

    for habit in habits:
        cur.execute(
            "INSERT INTO user_habits (user_id, habit, timestamp) VALUES (%s, %s, %s)",
            (habit['user_id'], habit['habit'], habit['timestamp'])
        )

    conn.commit()
    cur.close()
    conn.close()

# Fetch data from SQLite and send it to the data warehouse
sqlite_conn = sqlite3.connect('user_habits.db')
sqlite_cur = sqlite_conn.cursor()

sqlite_cur.execute("SELECT * FROM habits")
habits = sqlite_cur.fetchall()

send_to_data_warehouse(habits)