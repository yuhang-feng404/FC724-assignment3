from flask import Flask, render_template, redirect
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
    try:
        with open("feedback.txt", "r") as fp:
            final_data = fp.read().split("|")
            name = final_data[0]
            course = final_data[1]
            short_answer = final_data[2]
            long_answer = final_data[3]
            satisfaction = final_data[4]
            recommend = final_data[5]
            improvements = final_data[6]
    except FileNotFoundError:
        name = 'No feedback data found'
        course = 'Please submit your feedback'
        short_answer = 'No feedback data found'
        long_answer = 'Please submit your feedback'
        satisfaction = 'No feedback data found'
        recommend = 'Please submit your feedback'
        improvements = 'No feedback data found'

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
        name = form.name.data
        course = form.course.data
        short_answer = form.short_answer.data
        long_answer = form.long_answer.data
        satisfaction = form.satisfaction.data
        recommend = form.recommend.data
        improvements = form.improvements.data

        name = name.replace('|', '')
        course = course.replace('|', '')
        short_answer = short_answer.replace('|', '')
        long_answer = long_answer.replace('|', '')
        satisfaction = satisfaction.replace('|', '')
        recommend = recommend.replace('|', '')
        improvements = improvements.replace('|', '')
        final_data = name + "|" + course + "|" + short_answer + "|" + long_answer + "|" + satisfaction + "|" + recommend + "|" + improvements
        with open("feedback.txt", "w") as fp:
            fp.write(final_data)
        return redirect('/current_feedback')
    return render_template('data_collection.html', form=form)


if __name__ == '__main__':
    app.run()
