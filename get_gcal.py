#!/usr/bin/python
# coding: utf-8

# Using only stdlib to avoid package installation issues.
import datetime
import os.path
from urllib.request import urlopen

url_template = """https://www.googleapis.com/calendar/v3/calendars/admin%40daytontechevents.com/events?singleEvents=true&orderBy=startTime&timeMin={timeMin}&timeMax={timeMax}&key={google_api_key}"""

date_format = '%Y-%m-%dT12:00:00-04:00'

with open('google_api_key.txt') as infile:
    google_api_key = infile.read().strip()

start_date = datetime.datetime.now().strftime(date_format)
end_date = (datetime.datetime.now() + 
            datetime.timedelta(days=90)).strftime(date_format)

url = url_template.format(timeMin=start_date, timeMax=end_date, google_api_key=google_api_key)
result = urlopen(url)
contents = result.read()
with open(os.path.join('_data', 'events.json'), 'w') as outfile:
    outfile.write(contents.decode('utf8'))

