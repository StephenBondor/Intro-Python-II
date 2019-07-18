from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Huffy Attitude", "This is how business gets DONE."), Item("Big Haircut", "Very attractive")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south. There isn't even a manager to talk to."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room. DONE

# Write a loop that: DONE
#
# * Prints the current room name DONE
# * Prints the current description (the textwrap module might be useful here). DONE
# * Waits for user input and decides what to do. DONE
#
# If the user enters a cardinal direction, attempt to move to the room there. DONE
# Print an error message if the movement isn't allowed. DONE
#
# If the user enters "q", quit the game. DONE

player1 = Player("Karen", room["outside"], "Can I speak to your manager?")


while True:
    print(
        f'You are {player1.name}. You are at the {player1.location.name}. {player1.location.description}')
    user_input = input(
        "Enter an action, or don't, ultimately, you'll be talking to the manager (inspectnails for help): ").split(' ')
    if len(user_input) == 1:
        if user_input[0] == "y":
            print("Can I talk to your manager?")
        if user_input[0] == "q":
            print(f'{player1.name} could not find the manager. Goodbye.')
            break
        if user_input[0] == "n" or user_input[0] == "s" or user_input[0] == "e" or user_input[0] == "w":
            player1.move_to(user_input[0])
        if user_input[0] == "l":
            player1.look_around()
        if user_input[0] == "metime":
            player1.me_time()
    elif len(user_input) == 2:
        if user_input[0] == "g":
            player1.get_item(int(user_input[1]))
        if user_input[0] == "t":
            player1.trash_item(int(user_input[1]))
