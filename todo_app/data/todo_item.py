
class Item:

    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])

    # def reset(self):
    #     self.status = 'To Do'

    # def start(self):
    #     self.status = 'Doing'

    # def complete(self):
    #     self.status = 'Done'
