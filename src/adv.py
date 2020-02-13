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
    'potion': Item('potion', 'item that restores hp'),
    'jar': Item('jar', 'item useful for storing liquids')
}

room['outside'].items.append(item['wand'])
room['outside'].items.append(item['sword'])
room['outside'].items.append(item['bow'])
room['overlook'].items.append(item['potion'])
room['narrow'].items.append(item['jar'])

new_player = input('Please enter a name: ')

start = room['outside']

location = start

p = Player(new_player, start)

print(p)

room['outside'].current_items()

item_select = input('\nWhat is your weapon of choice? ')

while room['outside'].check_item(item_select) == 0:
    room['outside'].current_items()
    item_select = input('\nWhat is your weapon of choice? ')

p.inventory.append(item_select)

print('If you see an item type get \'item\' to add to inventory and drop \'item\' to remove from inventory')


def move():
    print(Player(new_player, location))
    if len(location.items) > 0 and location.items[0].name not in p.inventory:
        location.current_items()


# adds item to inventory and removes it from the room
def add_item(new_item):
    if len(location.items) > 0 and new_item not in p.inventory:
        p.inventory.append(new_item)
        print(f'{new_item} added to inventory')
        location.items.remove(item[new_item])


# removes desired item from inventory and adds it to the room
def drop_item(dropped_item):
    print(Player(new_player, location))
    p.inventory = [items for items in p.inventory if items != dropped_item]
    location.items.append(item[dropped_item])
    location.current_items()


while True:
    choice = input('Select direction or press i for inventory: ')

    if len(choice) > 1:
        choice = choice.split()

        if choice[0] == 'get':
            try:
                if choice[0] == 'get' and item[choice[1]] in location.items:
                    add_item(choice[1])
                else:
                    print('Please enter an item you currently in the room')
            except IndexError:
                print('Please enter a valid item you wish to add to your inventory')
        else:
            try:
                if choice[0] == 'drop' and choice[1] in p.inventory:
                    drop_item(choice[1])
                else:
                    print('Please enter an item you currently have in your inventory')
            except IndexError:
                print('Please enter a valid item you wish to remove from your inventory')

    else:
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
