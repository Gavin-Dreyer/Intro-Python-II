# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description

    def __str__(self):
        return '{self.room_name}. {self.description}'.format(self=self)
