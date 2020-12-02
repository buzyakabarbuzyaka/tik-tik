from typing import Optional

from pydantic import BaseModel


class ChannelBase(BaseModel):
    boobs: int = 0
    subscribers:  int = 0


class Channel(ChannelBase):
    id: int
    channel_name: str

    class Config:
        orm_mode = True
