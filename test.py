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
    print 'Event Object     ', event
    print 'Event Name       ', event.summary
    print 'Event Description', event.description
    print 'Event All Day?   ', event.allday
    print 'Event Start Date ', event.startDate
    print 'Event Start Time ', event.startTime
    print 'Event End Date   ', event.endDate
    print 'Event End Time   ', event.endTime
    print '\n'

print '\nadd_event'
print '*********'
cal = calap.list_calendars()[0]
print 'New event ID', calap.add_event(cal, event)

print '\n'