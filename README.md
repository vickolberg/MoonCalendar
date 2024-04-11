Moon Calendar

This simple and lightweight flask application tracks moon parameters in the format of a calendar.

This app tracks moon light, moon rise time, and moon set time.

You cannot go back in time for historical data in this application. When entering a start date, it must either be today or a date in the future. 

This app is written enirely in Python, HTML, and CSS. No JavaScript is required for this simple application.

The app uses a few different API calls:
The API call for https://nominatim.openstreetmap.org helps us convert city and state, taken from our users input, into latitude and longitude coordinates. This is required for our next API calls.
The API https://api.meteomatics.com/ is used in 3 separate instances. We are gathering 3 parameters, moon visibilty, moon rise, and moon set. These API requests require latitude and longitude, which we now have as a result of our last API request!
With each new search, a new API request is generated based on user input. We then write over the json files storing the API data, so it is up-to-date.
It is important to note that all the data received from our API is in JSON format. There are other options through meteomatics, but JSON was ideal for this project.

You might find yourself wondering, "How in the world is there a working calendar without any JavaScript?!" I'll tell you how- because we don't need it. Instead, we can import calendar, a python library that is built in to python3! This is much lighter weight than using something like FullCalendar.js

I would not recommend using this for larger applications, where FullCalendar.js would be more beneficial.

The CSS styling was not entirely my own creation. My 7-year old daughter chose all the styles for the website after I completed the backend application. She did a fantastic job and deserves the credit for her creativity! Go Nina!