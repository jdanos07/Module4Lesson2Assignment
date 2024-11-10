class Event:
        def __init__(self, name, date, participant_count):
            self.name = name
            self.date = date
            self.participant_count = participant_count

        def add_participant(self, new_participant_count):
            self.participant_count = new_participant_count
        
        def display_participant_count(self):
            print(f'Event: {self.name}, on {self.date} has {self.participant_count} participants.')

event = {}
import re

def event_detials(name, date, participant_count):
     event[name] = Event(name, date, participant_count)
     print(f'Event: "{name}" has been scheduled for {date}. {participant_count} individuals will be in attendance.')

def update_participant_count(name, new_participant_count):
     if name in event:
          event[name].add_participant(new_participant_count)
          print(f'Event attendance has been updated to {new_participant_count}')
        
def display_participant_count():
     for participant in event.values():
          participant.display_participant_count()

def date_format(date_input):
     format = r'\d{1,2}/\d{1,2}/\d{4}$'
     if re.match(format, date_input):
          return True
     else:
          return False