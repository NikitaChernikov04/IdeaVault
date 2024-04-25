import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import RegistrationForm, LoginForm, IdeaForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gen_user:ilyxneilyx13@147.45.148.62/django_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


@app.route('/')
def main():
    return render_template('main.html')


class MyUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate:
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:
            return "Пароли не совпадают, попробуйте еще раз"

        # Проверка наличия пользователя в базе данных
        existing_user = MyUsers.query.filter_by(username=username).first()
        if existing_user:
            return "Пользователь с таким именем уже существует"

        # Добавление пользователя в базу данных
        new_user = MyUsers(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

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
        return f"username: {form.username.data}, Password: {form.password.data}"
    return render_template('login.html', form=form)


# @app.route('/reset', methods=['GET', 'POST'])
# def reset():
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         return f"Email: {form.email.data} - Запрос на восстановление пароля отправлен"
#     return render_template('reset_pass.html', form=form)


@app.route('/search_card')
def search_card():
    # Получение данных о карточках из базы данных
    cards = Idea.query.all()
    return render_template('search_card.html', cards=cards)


@app.route('/create', methods=['GET', 'POST'])
def create_idea():
    form = IdeaForm()
    if form.validate_on_submit():
        idea_text = form.idea.data
        image = form.image.data

        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_url = os.path.join('uploads', filename)
        else:
            image_url = 'static/img/default.jpg'  # путь к изображению по умолчанию

        new_idea = Idea(content=idea_text, image_url=image_url)
        db.session.add(new_idea)
        db.session.commit()

        flash('Idea created successfully!', 'success')
        return redirect(url_for('create_idea'))
    return render_template('card_form.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
