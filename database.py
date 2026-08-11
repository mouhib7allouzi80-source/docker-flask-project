import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )


def init_db():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL
        )
    """)

    conn.commit()

    cursor.close()
    conn.close()


def add_task(title):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(title) VALUES(%s)",
        (title,)
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_tasks():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return tasks


def get_task(task_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id=%s",
        (task_id,)
    )

    task = cursor.fetchone()

    cursor.close()
    conn.close()

    return task


def update_task(task_id, title):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET title=%s WHERE id=%s",
        (title, task_id)
    )

    conn.commit()

    cursor.close()
    conn.close()


def delete_task(task_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=%s",
        (task_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()
