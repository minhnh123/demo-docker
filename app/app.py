from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_tasks, add_task, delete_task, update_task_status

app = Flask(__name__)

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_name = request.form['task_name']
    add_task(task_name)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>')
def update(task_id):
    update_task_status(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
