CalAp
=====

API wrapper for Google Calendar with OAuth 2 authentication

This project requires a `client_secrets.json` file. This file is may be obtained
from google at: https://developers.google.com/google-apps/calendar/get_started.
Using the Quickstart Configuration tool, select Python/Command Line and create a
new project. Download the client secrets file.

## Usage

Import the app with `from calap import CalAp` and initialize it with `calap = CalAp()`.

### list_calendars()
Returns all calendars as a list of `calendar` objects.

### list_events(calendar)
Returns names of all events in a given `calendar` as a list of strings. 

### get_events(calendar)
Returns all events in a given `calendar` as a list of `Event` objects.

### Event objects
Event objects are returned by `get_events()` and have the following properties:

- summary
- description
- allday
- startDate
- startTime
- endDate
- endTime
