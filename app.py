from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import RegistrationForm, LoginForm, ResetPasswordForm, IdeaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key_here'
bootstrap = Bootstrap(app)

@app.route('/main')
@app.route('/')
def main():
    return render_template('main.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate:
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:
            return "Пароли не совпадают, попробуйте еще раз"

        # Здесь можно добавить логику для обработки данных, например, сохранение в базу данных

        return render_template('registration_success.html', username=username)
    else:
        return render_template('registration.html', form=form)


@app.route('/success')
def success():
    return render_template('registration_success.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return f"Email: {form.email.data}, Password: {form.password.data}"
    return render_template('login.html', form=form)


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        return f"Email: {form.email.data} - Запрос на восстановление пароля отправлен"
    return render_template('reset_pass.html', form=form)


@app.route('/search_card')
def search_card():
    # Ваша логика для получения данных о карточках
    card = {
        'image_url': '/path/to/image.jpg',
        'title': 'Card Title',
        'content': 'Some quick example text to build on the card title and make up the bulk of the card\'s content.'
    }
    return render_template('search_card.html', card=card)


@app.route('/create', methods=['GET', 'POST'])
def create_idea():
    form = IdeaForm()
    if form.validate_on_submit():
        # Действия при успешном сохранении идеи
        flash('Idea created successfully!', 'success')
        return redirect(url_for('create_idea'))
    return render_template('card_form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)