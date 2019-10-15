from flask import Flask
from flask import render_template, flash, redirect, url_for
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Shawn"}
    posts = [
        {
            'author': {'username': 'Bob'},
            'body': 'Bobs your uncle'
        },
        {
            'author': {'username': 'Tiff'},
            'body': 'Like, I totally like cheetos. For real.'
        }
    ]
    return render_template('index.html', title='lame users talk', user=user, posts=posts)


@app.route('/backpack')
def backpack():
    user = {'username': "Shawn"}
    my_backpack = [
        {'type': 'sword',
         'name': 'Sting'},
        {
         'type': 'dagger',
         'name': 'Dagger +1'
        }
    ]
    return render_template('backpack.html', title='Backpack', user=user, backpack=my_backpack)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run()
