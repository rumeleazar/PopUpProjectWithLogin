from flask import Flask, render_template, session, url_for, flash, redirect, request
import sqlite3
from datetime import timedelta, date

app = Flask(__name__)
app.secret_key = 'MySecretKey'
app.permanent_session_lifetime = timedelta(hours=0.5)


@app.route('/', methods=['POST', 'GET'])
def index():

    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM votes WHERE vote = 'no'")
        NoVotes = cur.fetchall()

        cur = conn.cursor()
        cur.execute("SELECT * FROM votes WHERE vote = 'yes'")
        YesVotes = cur.fetchall()

        if request.method == 'POST':
            vote = request.form['radiobutton']
            username = session['username']

            cur.execute("INSERT INTO votes(vote,username) VALUES(?, ?)",
                        (vote, username))
            conn.commit()
            cur.close()
            cur = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM votes WHERE vote = 'no'")
            NoVotes = cur.fetchall()

            cur = conn.cursor()
            cur.execute("SELECT * FROM votes WHERE vote = 'yes'")
            YesVotes = cur.fetchall()
            return render_template("index.html", yes=YesVotes, no=NoVotes, username=session['username'])

        return render_template("index.html", yes=YesVotes, no=NoVotes)


@app.route('/admin', methods=['POST', 'GET'])
def admin():

    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM votes WHERE vote = 'no'")
        NoVotes = cur.fetchall()

        cur = conn.cursor()
        cur.execute("SELECT * FROM votes WHERE vote = 'yes'")
        YesVotes = cur.fetchall()

    return render_template("admin.html", yes=YesVotes, no=NoVotes)


@app.route('/register', methods=['POST', 'GET'])
def register():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT username FROM user")
        user = cur.fetchall()

        if request.method == 'POST':
            if request.form['username'] == '' or request.form['password'] == '' or request.form['name'] == '':
                flash('Please fill up all the forms')
                return redirect(url_for('register'))

            else:
                for x in user:
                    if request.form['username'] == x[0]:
                        flash('Username already taken')
                        return redirect(url_for('register'))

                username = request.form['username']
                password = request.form['password']
                name = request.form['name']

                cur = conn.cursor()
                cur.execute("INSERT INTO user(username, password,name) VALUES(?, ?, ?)",
                            (username, password, name))
                conn.commit()
                cur.close()
                flash('Registration Complete')
                return redirect(url_for('login'))

        return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

    with sqlite3.connect('database.db') as conn:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            session.permanent = True
            username = request.form['username']
            password = request.form['password']
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
            account = cur.fetchone()

            if account:
                if username == 'admin':
                    session['loggedin'] = True
                    session['username'] = username
                    session['password'] = password
                    return redirect(url_for('admin'))

                else:
                    session['loggedin'] = True
                    session['username'] = username
                    session['password'] = password
                    return redirect(url_for('index', username=username))

            else:
                flash('Incorrect Username or Password')
                return redirect(url_for('login'))

        return render_template('login.html')


# ROUTE FOR THE LOGOUT BUTTON
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have successfully logged out')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
