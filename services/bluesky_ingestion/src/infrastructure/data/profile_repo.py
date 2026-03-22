import os
import requests

class ProfileRepo():

    def __init__(self):
        self._endpoint = os.environ['account_endpoint']

    def get_profile(self):
        pass