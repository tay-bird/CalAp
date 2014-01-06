#! /usr/bin/env python

from api_app import main

class CalAp():
    
    def __init__(self):
        self.service = main()

    def list_calendars(self):
        page_token = None
        results = []
        while True:
            calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                results.append(calendar_list_entry['summary'])
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
        return results

    def list_events(self, calendarId):
        page_token = None
        results = []
        while True:
            events = self.service.events().list(calendarId=calendarId, pageToken=page_token).execute()
            for event in events['items']:
                results.append(event['summary'])
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        return results
    
    def get_events(self, calendarId):
        page_token = None
        results = []
        while True:
            events = self.service.events().list(calendarId=calendarId, pageToken=page_token).execute()
            for event in events['items']:
                results.append(event)
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        return results