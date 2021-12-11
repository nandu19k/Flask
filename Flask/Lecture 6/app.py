from flask import Flask, redirect, url_for , render_template, request , session
from datetime import timedelta 
from flask import flash


app = Flask(__name__)
app.secret_key = "nerchuko"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("home.html")   

@app.route("/login" , methods = ["POST" , "GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['usr_name']
        session['user'] = user 
        flash("Login Successful !!") 
        return redirect(url_for("user" )) 
    else:
        if "user" in session:
            flash("You are already logged in !!") 
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route('/user')
def user():
    if 'user' in session:
        user = session['user'] 
        return render_template("user.html" , user = user) 
    else: 
        flash("you are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user" , None)
    flash("You have been logged out!" , 'info') 
    return redirect(url_for("login"))
 
if __name__ == '__main__':
    app.run(debug = True)