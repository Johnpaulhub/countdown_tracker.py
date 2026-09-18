from flask import Flask, request, redirect, url_for

app = Flask(__name__)

TASKS = [
    {"id": 1, "title": "Flask Portfolio Deployment", "deadline": "2026-09-25", "priority": "High"}
]

@app.route('/')
def countdown_home():
    task_html = ""
    for t in TASKS:
        color = "#f43f5e" if t['priority'] == "High" else "#38bdf8"
        task_html += f'''
        <div style="background: #1b2230; border-radius: 8px; padding: 12px; margin-bottom: 10px; border: 1px solid #2a3447; border-left: 4px solid {color};">
            <div style="font-size: 14px; font-weight: bold; color: #fff;">{t['title']}</div>
            <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">Due Date: <span style="color: #fff;">{t['deadline']}</span> | Priority: <span style="color: {color}; font-weight: bold;">{t['priority']}</span></div>
        </div>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Countdown Tracker</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: sans-serif; background: #121824; color: #fff; margin: 0; padding: 12px; }}
            h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 6px; }}
            .card {{ background: #1b2230; padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #2a3447; }}
            input, select {{ width: 100%; padding: 10px; margin: 6px 0 12px 0; background: #121824; border: 1px solid #334155; color: #fff; border-radius: 6px; box-sizing: border-box; }}
            button {{ width: 100%; padding: 12px; background: #10b981; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        <h2>Assignment & Exam Tracker</h2>
        <div class="card">
            <h3 style="margin-top:0; color:#10b981; font-size:15px;">Add New Milestone</h3>
            <form action="/add_task" method="POST">
                <input type="text" name="title" placeholder="Task / Exam Title" required>
                <input type="date" name="deadline" required>
                <select name="priority">
                    <option value="High">High Priority</option>
                    <option value="Medium">Medium Priority</option>
                    <option value="Low">Low Priority</option>
                </select>
                <button type="submit">+ Add Milestone</button>
            </form>
        </div>
        <h3 style="color: #38bdf8; margin-top: 20px;">Active Countdowns</h3>
        {task_html}
    </body>
    </html>
    '''

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    deadline = request.form.get('deadline')
    priority = request.form.get('priority')
    if title and deadline:
        TASKS.append({"id": len(TASKS) + 1, "title": title, "deadline": deadline, "priority": priority})
    return redirect(url_for('countdown_home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
