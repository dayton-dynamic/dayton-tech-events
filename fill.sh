#! /bin/bash
curl -o _data/events.json https://www.googleapis.com/calendar/v3/calendars/admin%40daytontechevents.com/events?singleEvents=true&orderBy=startTime&timeMin=$(date +'%Y-%m-%dT12:00:00-04:00')&timeMax=$(date +'%Y-%m-%dT12:00:00-04:00' -d "+90 days")&key=AIzaSyCOFBWPX-qF1KaYvflBWdRT989b2HioIQo
