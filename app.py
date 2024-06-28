from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome_page():  # put application's code here
    return render_template('welcome.html')


@app.route('/information')
def information_page():  # put application's code here
    return render_template('information.html')


@app.route('/data_collection')
def data_collection_page():  # put application's code here
    return render_template('data_collection.html')


if __name__ == '__main__':
    app.run()
