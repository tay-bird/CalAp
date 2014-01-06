CalAp
=====

API wrapper for Google Calendar with OAuth 2 authentication

These project files must be placed in the Google Calendar API Quickstart Application directory.

This app may be downloaded from: https://developers.google.com/google-apps/calendar/get_started

## Usage

Import the app with `from calap import CalAp` and initialize it with `calap = CalAp()`.

### list_calendars()
Returns all calendars as a list of `calendar` objects.

### list_events(calendar)
Returns names of all events in a given `calendar` as a list of strings. 

### get_events(calendar)
Returns all events in a given `calendar` as a list of `Event` objects.

### Event objects
Event objects are returned by `get_events` and have the following properties:

- summary
- description
- allday
- startDate
- startTime
- endDate
- endTime
