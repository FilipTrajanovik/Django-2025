import os
import django

# ✅ Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")

# ✅ Initialize Django
django.setup()

from fastapi import FastAPI
from tasks.models import Task
from django.forms.models import model_to_dict
import sqlite3

app = FastAPI()

@app.get("/api/tasks/")
def get_tasks():
    tasks = Task.objects.all()
    return [model_to_dict(task) for task in tasks]

connection=sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL,
    )
""")
connection.commit()

cursor.execute("INSERT INTO tasks VALUES (%s, %s, %s)", ("Labs", "Vo 5", "DONE"))
connection.commit()