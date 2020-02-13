from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Items

item = {
    'wand': Item('wand', 'ranged weapon with weak damage, but increases player\'s spell power'),
    'sword': Item('sword', 'close range combat weapon with high damage'),
    'bow': Item('bow', 'ranged weapon with high damage'),
    'potion': Item('potion', 'restores hp')
}

room['outside'].items.append(item['wand'])
room['outside'].items.append(item['sword'])
room['outside'].items.append(item['bow'])


# new_player = input('Please enter a name: ')

start = room['outside']
location = start

p = Player('joe', start)

print(p)
room['outside'].current_items()

item_select = input('\nWhat is your weapon of choice? ')

while room['outside'].check_item(item_select) == 0:
    item_select = input('\nWhat is your weapon of choice? ')

p.inventory.append(item_select)


def move():
    print(Player('Joe', location))


while True:
    choice = input('Select direction or press i for inventory: ')

    if choice == 'n':
        try:
            hasattr(location, 'n_to') == False
            location = location.n_to
        except AttributeError:
            print("Please enter a valid direction")
            continue

        move()

    if choice == 's':
        try:
            hasattr(location, 's_to') == False
            location = location.s_to
        except AttributeError:
            print("Please enter a valid direction")
            continue

        move()

    if choice == 'e':
        try:
            hasattr(location, 'e_to') == False
            location = location.e_to
        except AttributeError:
            print("Please enter a valid direction")
            continue

        move()

    if choice == 'w':
        try:
            hasattr(location, 'w_to') == False
            location = location.w_to
        except AttributeError:
            print("Please enter a valid direction")
            continue

        move()

    if choice == 'i':
        p.current_inventory()

    if choice == 'q':
        break
