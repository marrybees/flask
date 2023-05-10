from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    x = [sleep, walk, run]
    return render_template('index.html',x = x )

@app.route('/user/<name>/<age>')
def user(name, age):
    information  = [m for m in range(1, age+1) if age % m == 0]
    return render_template('user.html', name=name, information = information)

if __name__ == '__main__':
    app.run(debug=True)