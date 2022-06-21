from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open_time = StringField('Open time', validators=[DataRequired()])
    close_time = StringField('Closing time', validators=[DataRequired()])
    rate_coffee = SelectField('Rate the coffee', validators=[DataRequired()], choices=['☕️☕️☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️', '☕️☕️', '☕️'])
    rate_wifi = SelectField('Rate the Wi-Fi', validators=[DataRequired()], choices=['💪💪💪💪💪', '💪💪💪💪', '💪💪💪', '💪💪', '💪', '✘'])
    rate_power = SelectField('Rate the 🔌 availability', validators=[DataRequired()], choices=['🔌🔌🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌', '🔌🔌',' 🔌'])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        print(type(form),"form")
        form_entry = [entry.data for entry in form][:-2]
        form_entry[0] = '\n' + form_entry[0]
        with open('cafe-data.csv', mode='a') as data_file:
            entry_data = (',').join(form_entry)
            data_file.write(entry_data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
