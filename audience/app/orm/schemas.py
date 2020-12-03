from typing import Optional

from pydantic import BaseModel


class NewChannel(BaseModel):
    id: Optional[int]
    channel_name: str
    boobs: Optional[int] = 0
    subscribers: Optional[int] = 0


class ChannelBase(BaseModel):
    boobs: int = 0
    subscribers:  int = 0


class Channel(ChannelBase):
    id: Optional[int]
    channel_name: str

    class Config:
        orm_mode = True
