import eventManagement as event

while True:
    action = input('Enter Action (Create, Edit, Display, Exit) ').lower()
    if action == 'exit':
        break
    try:
        if action == 'create':
            name = input('Enter event name: ')
            while True:
                date = input('Enter event date: ')
                if event.date_format(date):
                    break
                else:
                    print('Invalid format. Use mm/dd/yyyy formatting.')
            participant_count = input('Enter expected event attendance: ')
            event.event_detials(name, date, participant_count)
        elif action == 'edit':
            event.display_participant_count()
            selected_event = input('Enter event name that needs the attendace updated: ').lower()
            if selected_event in event.event:
                new_participant_count = int(input('Enter new participant count: '))
                event.update_participant_count(selected_event, new_participant_count)
            else:
                print('This event does not exist.')
        elif action == 'display':
            event.display_participant_count()
    except Exception as e:
        print(f'Error: {e}')