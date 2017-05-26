import requests


class RequestHandler:

    def __init__(self):
        self.api = 'https://en.wikipedia.org/w/api.php'
        self.payload = {'action': 'query', 'generator': 'allpages'}
