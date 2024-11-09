import vehicleReg as vr

while True:
    action = input('Enter Action (register, update, display, exit) ').lower()
    if action == 'exit':
        break

    try:
        if action == 'register': 
            vehicle_type = input('Enter vehicle type: ')
            owner = input('Enter owner name: ')
            vr.register(vehicle_type, owner)
        elif action == 'update':
            vr.display_all_regos()
            reg_num = input('Enter registation number to be updated ')
            new_owner = input('Enter new owners name: ')
            vr.update_vehicle_owner(reg_num, new_owner)
        elif action == 'display':
            vr.display_all_regos()       
    except Exception as e:
        print(f'Error: {e}')