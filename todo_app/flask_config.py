import os


class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")

    """Base configuration variables."""
    TRELLO_BASE_URL = 'https://api.trello.com/1'
    TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
    TRELLO_API_SECRET = os.environ.get('TRELLO_API_SECRET')
    TRELLO_BOARD_ID = os.environ.get('TRELLO_BOARD_ID')

