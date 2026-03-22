import json
import logging
import websockets

from ..queues.firehose_queue import FirehoseQueue
from ..models.firehose_post import FirehosePostResponse

class BlueskyFirehoseStream():

    def __init__(self, uri : str,  queue : FirehoseQueue):
        self._uri = uri
        self._queue = queue
        self._logger = logging.getLogger(self.__class__.__name__)

    async def start(self):
        async with websockets.connect('ws://localhost:8765') as websocket:
            message = "Hello, Server!"
            await websocket.send(message)
            response = await websocket.recv()
            json_response = json.loads(response)
            self._logger.debug(f"Received response")
            await self._queue.put(FirehosePostResponse(**json_response))