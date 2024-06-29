from flask import Flask, render_template
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
csrf = CSRFProtect(app)


class StudentFeedbackForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    course = StringField('Course:', validators=[DataRequired()])
    short_answer = TextAreaField('Short-form Answer:', validators=[DataRequired()])
    long_answer = TextAreaField('Long-form Answer:', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction:', choices=[
        ('', 'Select Satisfaction Level'),
        ('very-satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('unsatisfied', 'Unsatisfied'),
        ('very-unsatisfied', 'Very Unsatisfied')
    ], validators=[DataRequired()])
    recommend = RadioField('Would you recommend this course to others?', choices=[
        ('yes', 'Yes'),
        ('no', 'No')
    ], validators=[DataRequired()])
    improvements = TextAreaField('Suggestions for Improvement:')


@app.route('/')
def welcome_page():  # put application's code here
    return render_template('welcome.html')


@app.route('/information')
def information_page():  # put application's code here
    return render_template('information.html')


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


@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = StudentFeedbackForm()
    if form.validate_on_submit():
        # process the form data here
        name = form.name.data
        course = form.course.data
        short_answer = form.short_answer.data
        long_answer = form.long_answer.data
        satisfaction = form.satisfaction.data
        recommend = form.recommend.data
        improvements = form.improvements.data
        # do something with the data
        return 'Thank you for submitting your feedback!'
    return render_template('data_collection.html', form=form)


if __name__ == '__main__':
    app.run()
