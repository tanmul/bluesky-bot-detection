import json
import logging
import websockets

from ..queues.firehose_queue import FirehoseQueue
from ..models.bluesky_post import BlueskyPost

class BlueskyFirehoseStream():

    def __init__(self, uri : str,  queue : FirehoseQueue):
        self._uri = uri
        self._queue = queue
        self._logger = logging.getLogger(self.__class__.__name__)

    async def start(self):
        async with websockets.connect(self._uri) as websocket:
            for i in range(6):
                response = await websocket.recv()
                json_response = json.loads(response)
                print(f"Received response: {json_response}")
                await self._queue.put(BlueskyPost(**json_response))