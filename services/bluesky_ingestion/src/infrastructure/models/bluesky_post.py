from pydantic import BaseModel, Field

class BlueskyPost(BaseModel):
    did : str = Field(alias='did')
    time_us : int = Field(alias='time_us')
    kind : str = Field(alias='kind')
    commit : dict = Field(alias='commit')