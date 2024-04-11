import json

def clean_visible_moon_data(json_file_path):
    moon_values = {}
    with open(json_file_path, 'r') as visible_moon_api:
        visible_moon_data = json.load(visible_moon_api)
        dates = visible_moon_data["data"][0]["coordinates"][0]["dates"]
        for date in dates:
            moon_values[date["date"]] = int(round(date["value"]))
    return moon_values

def clean_moon_rise_data(json_file_path2):
    moon_rise = {}        
    with open(json_file_path2, 'r') as moon_rise_api:
        moon_rise_data = json.load(moon_rise_api)
        dates = moon_rise_data["data"][0]["coordinates"][0]["dates"]
        for data in dates:
            try:
                date = data["date"].split("T")[0]
                time = data["value"].split("T")[1][:5]
                moon_rise[date] = time
            except IndexError as e:
                print("Error:", e)
                print("Problematic data:", data)
    return moon_rise

def clean_moon_set_data(json_file_path3):
    moon_set = {}        
    with open(json_file_path3, 'r') as moon_set_api:
        moon_set_data = json.load(moon_set_api)
        dates = moon_set_data["data"][0]["coordinates"][0]["dates"]
        for data in dates:
            try:
                date = data["date"].split("T")[0]
                time = data["value"].split("T")[1][:5]
                moon_set[date] = time
            except IndexError as e:
                print("Error:", e)
                print("Problematic data:", data)
    return moon_set