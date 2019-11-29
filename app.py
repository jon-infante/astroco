from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Home')

@app.route('/sun')
def sun():
    """Return Sunrise/Sunset Page"""
    return render_template('sun.html')

@app.route('/stars')
def stars():
    """Return Stars Page"""
    return render_template('stars.html')


if __name__ == '__main__':
    app.run(debug=True)
