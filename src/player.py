# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, player_name, current_room):
        self.player_name = player_name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return '\n{self.player_name} is currently at the {self.current_room}'.format(self=self)

    def current_inventory(self):
        print('\nCurrently in your inventory you have...')
        for i in range(len(self.inventory)):
            print(f'{self.inventory[i]}')
