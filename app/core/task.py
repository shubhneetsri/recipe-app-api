from app.celery_app import app
from datetime import datetime

@app.task
def say_hello():
    print("👋 Hello from Celery!")

@app.task
def print_time():
    print("🕒 Current time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))