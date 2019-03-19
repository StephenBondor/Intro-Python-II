class Item:
    def __init__(self, name, description):  # constructor
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'

    def on_take(self):
        print("This does not meet my expectations")

    def on_drop(self):
        print("I didn't want that anyway")
