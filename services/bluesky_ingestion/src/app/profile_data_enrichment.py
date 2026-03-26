from ..infrastructure.data import bluesky_profile_repo
from ..infrastructure.models import bluesky_post

import asyncio

# TODO: Look into other design patterns aside from a pipeline of enrichments
class ProfileDataEnrichmentService:
    """
    Will be used to enrich the post data retrieved from the firehose
    with profile data gathered from the ProfileRepo class
    """

    def __init__(self, profile_repo : bluesky_profile_repo.ProfileRepo, queue : asyncio.Queue):
        self._profile_repo = profile_repo
        self._queue = queue

    async def enrich(self):
        while True:
            post_model : bluesky_post.BlueskyPost = await self._queue.get()
            profile_model = self._profile_repo.get_profile(post_model.did)
            yield profile_model
            
