# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description
        self.items = []

    def __str__(self):
        return '{self.room_name}. {self.description}.\n'.format(self=self)

    def current_items(self):
        print('Items available in this area are: ')
        for i in range(len(self.items)):
            print(
                f'{self.items[i].name}:  {self.items[i].name} is a {self.items[i].description}')

    # checking to see if the user put in the correct input
    def check_item(self, item):
        count = 0
        for i in range(len(self.items)):
            if item == self.items[i].name:
                count += 1
        if count > 0:
            print(f'\n{item} was added to inventory\n')
            return 1
        else:
            print('\nPlease select a valid option\n')
            return 0
