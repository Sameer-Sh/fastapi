from builtins import str
from enum import Enum
from pydantic import BaseModel


class PlayerID(str, Enum):
    a = 'a'
    b = 'b'

class StartGameParams(BaseModel):
    field_size: int

class ViewFieldParams(BaseModel):
    field_id: int

class AddShipParams(BaseModel):
    field_id: int
    player_id: PlayerID
    x1: int
    y1: int
    x2: int
    y2: int

class FireOpponent(BaseModel):
    field_id: int
    player_id: PlayerID
    opponent_id: PlayerID
    x: int
    y: int