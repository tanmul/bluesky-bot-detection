import os
import logging
import requests
from typing import Dict, List, Any

from ..models.bluesky_profile import BlueskyProfile

class ProfileRepo():

    def __init__(self):
        self._endpoint = os.environ['account_endpoint']
        self._cached_profiles : Dict[str, BlueskyProfile]

    def get_profile(self, did : str):
        if did in self._cached_profiles:
            resp = requests.get('https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile', params={'actor': did})
            resp.raise_for_status()
            self._cached_profiles[did] = BlueskyProfile(**resp.json())
        return self._cached_profiles[did]