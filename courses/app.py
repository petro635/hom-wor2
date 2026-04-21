from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    # Просто повертаємо головну сторінку
    return render_template('index.html')

@app.route('/buy/<course_name>')
def buy_course(course_name):
    # Флеш-повідомлення про покупку
    flash(f"Вітаю! Ви успішно придбали курс: {course_name}", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)