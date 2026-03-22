import logging
from asyncio import Queue

class FirehoseQueue(Queue):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = logging.getLogger(self.__class__.__name__)