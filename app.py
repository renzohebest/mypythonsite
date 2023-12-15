from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/renzo')
def aboutr():
    return '<h1>About   renzo</h1>'


@app.route('/fer')
def aboutf():
    return '<h1>About FEr</h1>'
if __name__ == '__main__':
    app.run(debug=True)