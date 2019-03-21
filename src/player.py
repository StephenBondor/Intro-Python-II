# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, catchphrase, items=None):  # constructor
        self.name = name
        self.location = location
        self.catchphrase = catchphrase
        if items == None:
            self.items = []
        else:
            self.items = items

    def move_to(self, new_location):
        if getattr(self.location, f'{new_location}_to') != None:
            self.location = getattr(self.location, f'{new_location}_to')
        else:
            print("Sorry, no manager in that direction")

    def look_around(self):
        print(f'Looks for manager, sees: ')
        for i, item in enumerate(self.location.items):
            print(f'{i}: {item}')

    def me_time(self):
        print(f'{self.name} is ~super~ important, she has: ')
        for i, item in enumerate(self.items):
            print(f'{i}: {item}')

    def get_item(self, item_number):
        if len(self.location.items) > item_number and item_number >= 0:
            item = self.location.items.pop(item_number)
            item.on_take()
            self.items.append(item)
        else:
            print("We seriously need to find the manager, this is not OK")

    def trash_item(self, item_number):
        if len(self.items) > item_number and item_number >= 0:
            item = self.items.pop(item_number)
            item.on_drop()
            self.location.items.append(item)
        else:
            print("I seriously need to find the manager, this is like not OK")
