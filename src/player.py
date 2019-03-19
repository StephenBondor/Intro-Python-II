# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, catchphrase, items=[]):  # constructor
        self.name = name
        self.location = location
        self.catchphrase = catchphrase
        self.items = items
