from todo_app.data.todo_item import Item 

import requests
from flask import current_app as app


def get_key_token_params():
    return { 'key': app.config['TRELLO_API_KEY'], 'token': app.config['TRELLO_API_TOKEN'] }

def build_url(endpoint):
    return app.config['TRELLO_BASE_URL'] + endpoint

def build_params(params = {}):
    full_params = get_key_token_params()
    full_params.update(params)
    return full_params




# Get list on a Board, return lists
def get_lists():
    params = build_params({ 'cards': 'open' })  # retun open cards
    url = build_url('/boards/' + app.config['TRELLO_BOARD_ID'] + '/lists')
    response = requests.get(url, params = params)
    lists = response.json()

    return lists


# Get a list with a specified name
def get_list(name):
    lists = get_lists()
    for list in lists :
        if list['name'] == name :
            return list 


# get a list of cards
def get_items():
    lists = get_lists()
    items = []
    for card_list in lists:
        for card in card_list['cards']:
            items.append(Item.from_trello_card(card, card_list))

    return items


# get a card with ID
def get_item(id):
    items = get_items()
    for item in items:
        if item['id'] == id :
            return item 



# create a card with a name, default is to do list
def add_item(name):
    # get the id of the to do list 
    todo_list = get_list('To Do')
    params = build_params({ 'name': name, 'idList': todo_list['id'] })

    url = build_url('/cards')

    response = requests.post(url, params = params)
    card = response.json()

    return Item.from_trello_card(card, todo_list)


# start a item with a id, and move the item from to_do to doing
def start_item(id):
    doing_list = get_list('Doing')
    card = move_card_to_a_list(id, doing_list)

    return Item.from_trello_card(card, doing_list)

# done a item with id, and move the item from doing to done
def complete_item(id):

    done_list = get_list('Done')
    card = move_card_to_a_list(id, done_list)

    return Item.from_trello_card(card, done_list)

# move done item back to todo status with a id
def incomplete_item(id):
    todo_list = get_list('To Do')
    card = move_card_to_a_list(id, todo_list)

    return Item.from_trello_card(card, todo_list)


# this function to move item from one list to another list
def move_card_to_a_list(card_id, list):
    params = build_params({ 'idList': list['id'] })
    url = build_url('/cards/' + card_id)

    response = requests.put(url, params = params)
    return  response.json()

