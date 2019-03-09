import requests

class READSAPI:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url="https://www.goodreads.com/"