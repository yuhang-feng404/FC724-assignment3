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


@app.route('/current_feedback')
def current_feedback_submission():
    name = 'John Doe'
    course = 'Python Programming'
    short_answer = 'This course was great!'
    long_answer = 'I learned a lot from this course.'
    satisfaction = 'very-satisfied'
    recommend = 'yes'
    improvements = 'More exercises would be helpful.'

    return render_template('current_feedback.html',
                           name=name,
                           course=course,
                           short_answer=short_answer,
                           long_answer=long_answer,
                           satisfaction=satisfaction,
                           recommend=recommend,
                           improvements=improvements)


if __name__ == '__main__':
    app.run()
