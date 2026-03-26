from pydantic import BaseModel, Field
from typing import Dict, Any, List
from datetime import datetime

class BlueskyProfile(BaseModel):
    did: str = Field(alias='did')
    handle: str = Field(alias='handle')
    displayName: str = Field(alias='displayName')
    avatar: str = Field(alias='avatar')
    associated: Dict[str, Any]
    labels: List[Dict[str, Any]]
    createdAt: datetime
    description: str
    indexedAt: datetime
    followersCount: int
    followsCount: int
    postsCount: int