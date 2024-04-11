from flask import Flask, render_template, request, flash, redirect, get_flashed_messages
import json
import os
from clean_functions import clean_moon_rise_data, clean_visible_moon_data, clean_moon_set_data
import calendar
from secretkeys import secret_key

app = Flask(__name__)
app.secret_key = secret_key

my_data = {}
my_city = {}
my_state = {}

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        state = request.form.get("state")
        start_date = request.form.get("start_date")
        my_data["start_date"] = start_date
        my_city["city"] = city
        my_state["state"] = state
        from api_call_functions import fetch_moon_data
        fetch_moon_data(city, state, start_date)
        return redirect('/moon')
    flash("Welcome To Your Moon Tracking Adventure!")
    # Clear flashed messages after displaying them
    flashed_messages = get_flashed_messages()
    if flashed_messages:
        flashed_messages.clear()

    return render_template("index.html")
def month_convert(month):
    months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
    start_date = my_data.get("start_date", "")
    month = int(start_date[6])
    if 1 <= month <= 12:
        month_name = (months[month])
        return month_name

@app.route('/moon', methods=["POST", "GET"])
def page():
    start_date = my_data.get("start_date", "")
    year = int(start_date[0:4])
    month = int(start_date[6])
    cal = calendar.monthcalendar(year, month)
    city = my_city.get("city")
    state = my_state.get("state")
    json_file_path = os.path.join('static', 'data', 'visible_moon_api.json')
    json_file_path2 = os.path.join('static', 'data', 'moon_rise_api.json')
    json_file_path3 = os.path.join('static', 'data', 'moon_set_api.json')
    moon_values = clean_visible_moon_data(json_file_path)
    moon_rise = clean_moon_rise_data(json_file_path2)
    moon_set = clean_moon_set_data(json_file_path3)
    return render_template("moon.html", moon_values=moon_values, moon_rise=moon_rise, moon_set=moon_set, cal=cal, start_date=start_date, my_data=my_data, year=year, month=month, month_convert=month_convert, city=city, state=state)
    

if __name__ == '__main__':
    app.run(debug=True)
