import requests


class RequestHandler:

    def __init__(self):
        self.api = 'https://en.wikipedia.org/w/api.php'
        self.params = {'action': 'query', 'generator': 'allpages',
                        'prop': 'pageviews|info',
                        'gaplimit': '50', 'gapfrom': ''}

    def new_read(self):
        resp = requests.get(self.api, params=self.params)
        with open('pages.xml', 'w') as f:
            f.write(resp.text)