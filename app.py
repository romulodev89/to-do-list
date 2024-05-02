from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
