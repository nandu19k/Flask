from flask import Flask, redirect , url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to Nerchuko Youtube Channel </h1>"

@app.route("/courses")
def courses():
    return "Welcome to the Nerchuko Courses"

@app.route('/<name>')
def name(name):
    return f"Hello {name}!"

@app.route('/admin')
def admin():
    return redirect(url_for("courses"))

if __name__ == '__main__':
    app.run(debug = True)