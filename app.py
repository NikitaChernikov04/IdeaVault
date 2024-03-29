from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/main')
@app.route('/')
def main():
    return render_template('main.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Здесь можно добавить логику для обработки данных, например, сохранение в базу данных

        return render_template('registration_success.html', username=username)
    else:
        return render_template('registration.html')


@app.route('/success')
def success():
    return render_template('registration_success.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/reset')
def reset():
    return render_template('reset_pass.html')


if __name__ == '__main__':
    app.run(debug=True)