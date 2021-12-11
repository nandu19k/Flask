from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html" , content = ['ML' , 'DL' , 'CV', 'Python' , "Flask"])

@app.route('/index')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)