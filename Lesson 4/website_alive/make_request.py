"""Get a request"""


import requests


def make_req(website):
    response = requests.get(website)
    return response
