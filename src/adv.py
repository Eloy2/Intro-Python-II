from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [ Item("sword", "a long sword"), Item("lantern", "a small lantern"), Item("coat", "a big coat") ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [ Item("gun", "a shotgun"), Item("ring", "plain steel ring") ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [ Item("shells", "for the shotgun") ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [ Item("key", "a rusty key") ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [ Item("pencil", "a regular pencil"), Item("paper", "a note saying \"I got here first hehe\"") ]),
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

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Check for items in room
def items_in(items):
    if len(items) == 0:
        print("- There are no items.")
    else:
        for item in items:
            print(f"- {item.name.capitalize()}")


player = Player("Eloy", room["outside"])


on = True

while on:
    print(f"\nYou are in {player.current_room.name}")
    print(player.current_room.description)
    print("Items in room:")
    items_in(player.current_room.items)
    print("Enter i for Inventory, take [item] to take item, drop [item] to drop item, look [item] to get item description. Enter q to quit:")
    print("Enter n, s, e, w to go either north, south, east, or west:")
    player_input = input("")

    if len(player_input) == 1:
        if player_input == "q":
            on = False
        elif player_input == "i":
            print("\nInventory:") ###################################################### Inventory
            if len(player.items) == 0:
                print("There are no items in your Inventory.")
            else:
                items_in(player.items)
        elif player_input == "n":
            if hasattr(player.current_room, "n_to"):
                player.current_room = player.current_room.n_to
                continue
            else:
                print("\nThere is nothing that way.\n")
                continue
        elif player_input == "s":
            if hasattr(player.current_room, "s_to"):
                player.current_room = player.current_room.s_to
                continue
            else:
                print("\nThere is nothing that way.\n")
                continue
        elif player_input == "e":
            if hasattr(player.current_room, "e_to"):
                player.current_room = player.current_room.e_to
                continue
            else:
                print("\nThere is nothing that way.\n")
                continue
        elif player_input == "w":
            if hasattr(player.current_room, "w_to"):
                player.current_room = player.current_room.w_to
                continue
            else:
                print("\nThere is nothing that way.\n")
                continue
        else:
            print("\nI did not understand what you wrote.\n")
    else:
        if player_input[:4] == "take": ################################################################# Take item
            if player_input[5:] in [i.name for i in player.current_room.items]:
                for item in player.current_room.items:
                    if item.name == player_input[5:]:
                        player.items.append(item)
                        player.current_room.items.remove(item)
                        item.on_take()
                        continue
            else:
                print("\nThat item is not in this room.")
        elif player_input[:4] == "drop": ############################################################### Drop item
            if player_input[5:] in [i.name for i in player.items]:
                for item in player.items:
                    if item.name == player_input[5:]:
                        player.current_room.items.append(item)
                        player.items.remove(item)
                        item.on_drop()
                        continue
            else:
                print("\nThat item is not in your inventory.")
        elif player_input[:4] == "look": ################################################################# Look item
            if player_input[5:] in [i.name for i in player.items]:
                for item in player.items:
                    if item.name == player_input[5:]:
                        print("\n" + item.name.capitalize() + ":")
                        print(item.description)
            else:
                print("\nThat item is not in your inventory. Put it in your inventory to look at it.")
        else:
            print("\nI did not understand what you wrote.\n")




"""
while on: ################################################################################################## In outside
    player.current_room = "outside"
    player_input = parser()

    if player_input.lower() == "q":
        on = False

    elif player_input.lower() == "n":
        player.current_room = "overlook"
        ################################################################################################################################## In overlook
        while on:
            player.current_room = "overlook"
            player_input = parser()

            if player_input.lower() == "q":
                on = False

            elif player_input.lower() == "n":
                print("\nYou jumped into the chasm and died.\n")
                on = False

            elif player_input.lower() == "w":
                player.current_room = "foyer"
########################################################################################################################## In foyer
                while on:
                    player.current_room = "foyer"
                    player_input = parser()

                    if player_input.lower() == "q":
                        on = False

                    elif player_input.lower() == "n":
                        player.current_room = "narrow"
                        #################################################################################### In narrow
                        while on:
                            player.current_room = "narrow"
                            player_input = parser()

                            if player_input.lower() == "q":
                                on = False

                            elif player_input.lower() == "s":
                                break

                            elif player_input.lower() == "w":
                                player.current_room = "treasure"
                                ###################################################### In treasure
                                while on:
                                    player.current_room = "treasure"
                                    player_input = parser()

                                    if player_input.lower() == "q":
                                        on = False

                                    elif player_input.lower() == "e":
                                        break

                                    elif player_input.lower() == "n":
                                        print("You exited the cave. Thank you for playing!")
                                        on = False

                                    else:
                                        print("\nThere is nothing that way.\n")
                                        continue
######################################################################################### In treasure
                            else:
                                print("\nThere is nothing that way.\n")
                                continue
############################################################################################################## In narrow
                    elif player_input.lower() == "e":
                        break

                    else:
                        print("\nThere is nothing that way.\n")
                        continue
########################################################################################################################### In foyer
            elif player_input.lower() == "s":
                break

            else:
                print("\nThere is nothing that way.\n")
                continue
######################################################################################################################################### In overlook
    else:
        print("\nThere is nothing that way.\n")
        continue
"""
