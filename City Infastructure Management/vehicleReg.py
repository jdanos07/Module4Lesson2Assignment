class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
    
    def display_registration(self):
        print(f'Registration #{self.reg_number}: Type: {self.type}, Owner: {self.owner}')

registration = {}

def register(vehicle_type, owner):
    reg_num = f'{len(registration)+1}'
    if reg_num in registration:
        print('Cannot have duplicate registration numbers.')
        return
    registration[reg_num] = Vehicle(reg_num, vehicle_type, owner)
    print(f'Registration: {reg_num} successful.')

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in registration:
        registration[reg_num].update_owner(new_owner)
        print(f'Update owner for the vehicle {reg_num}.')
    else:
        print('Vehicle is not registered.')

def display_all_regos():
    for rego in registration.values():
        rego.display_registration()


