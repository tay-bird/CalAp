#! /usr/bin/env python

from calap import CalAp
from datetime import datetime

calap = CalAp()

print '\n'
print '*******'
print 'TESTING'
print '*******'

print '\nlist_calendars'
print '**************'
cals = calap.list_calendars()
for cal in cals:
    print cal

print '\nlist_events'
print '***********'
cal = calap.list_calendars()[0]
events = calap.list_events(cal)
for event in events:
    print event

print '\nget_events'
print '**********'
cal = calap.list_calendars()[0]
events = calap.get_events(cal)
for event in events:
    print event
    try:
        startTime = event['start'][u'dateTime']
    except KeyError:
        startTime = event['start']
    date = datetime.strptime(startTime.split("T")[0], '%Y-%m-%d')
    time = startTime.split("T")[1].split("-")[0]
    print date.year, date.month, date.day
    print time


print '\n'