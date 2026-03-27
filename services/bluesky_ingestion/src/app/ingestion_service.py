import asyncio
from typing import Any

class BlueskyIngestionService():

    def __init__(self, stream : Any, enrichment_service : Any):
        self._stream = stream
        self._enrichment_service = enrichment_service

    async def start(self):
        asyncio.create_task(self._stream.start())
        async for post, profile in self._enrichment_service.enrich():
            # This is where we will aggregate the post and profile and pass to the feature extraction
            print(post, profile)
