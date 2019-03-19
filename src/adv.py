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
        if user_input == ["y"]:
            print("Can I talk to your manager?")
        if user_input == ["q"]:
            print(f'{player1.name} could not find the manager. Goodbye')
            break
        if user_input == ["n"]:
            if player1.location.n_to != None:
                player1.location = player1.location.n_to
            else:
                print("Sorry, no manager in that direction")
        if user_input == ["e"]:
            if player1.location.e_to != None:
                player1.location = player1.location.e_to
            else:
                print("Sorry, no manager in that direction")
        if user_input == ["s"]:
            if player1.location.s_to != None:
                player1.location = player1.location.s_to
            else:
                print("Sorry, no manager in that direction")
        if user_input == ["w"]:
            if player1.location.w_to != None:
                player1.location = player1.location.w_to
            else:
                print("Sorry, no manager in that direction")
        if user_input == ["l"]:
            print(f'Looks for manager, sees: ')
            i = 0
            for item in player1.location.items:
                print(f'{i}: {item}')
                i = + 1
        if user_input == ["metime"]:
            print(f'{player1.name} is ~super~ important, she has: ')
            i = 0
            for item in player1.items:
                print(f'{i}: {item}')
                i = + 1
    elif len(user_input) == 2:
        if user_input[0] == "g":
            if len(player1.location.items) > int(user_input[1]) and int(user_input[1]) >= 0:
                item = player1.location.items.pop(int(user_input[1]))
                item.on_take()
                player1.items.append(item)
            else:
                print("We seriously need to find the manager, this is not OK")
        if user_input[0] == "t":
            if len(player1.items) > int(user_input[1]) and int(user_input[1]) >= 0:
                item = player1.items.pop(int(user_input[1]))
                item.on_drop()
                player1.location.items.append(item)
            else:
                print("We seriously need to find the manager, this is not OK")
