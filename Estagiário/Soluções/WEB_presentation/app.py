from flask import Flask
from flask import redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('main_page'))

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

@app.route('/item_01')
def item_01():
    return "item 01 page"

@app.route('/item_02')
def item_02():
    return "item 02 page"

@app.route('/item_03')
def item_03():
    return "item 03 page"

@app.route('/item_04')
def item_04():
    return "item 04 page"

@app.route('/item_05')
def item_05():
    return "item 05 page"

@app.route('/item_06')
def item_06():
    return "item 06 page"

if __name__ == '__main__':
    app.run(debug=True)