from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.battleship.battleship_params import AddShipParams, StartGameParams, ViewFieldParams
from app.services.battleship.interactions.add_ship import add_ship
from app.services.battleship.interactions.fire_opponent import fire_opponent
from app.services.battleship.interactions.start_game import start_game
from app.services.battleship.interactions.view_battle_field import view_battle_field


router = APIRouter(prefix = "/battleship",tags=["Battleship"])


@router.post('/start-game')
async def start_game_api(request: StartGameParams):
    response = start_game(vars(request))

    return JSONResponse(
        status_code = 200,
        content = response
    )

@router.post('/view-battle-field')
async def view_battle_field_api(request: ViewFieldParams):
    response = view_battle_field(vars(request))

    return JSONResponse(
        status_code = 200,
        content = response
    )

@router.post('/add-ship')
async def add_ship_api(request: AddShipParams):
    response = add_ship(vars(request))

    return JSONResponse(
        status_code = 200,
        content = response
    )

@router.post('/fire-opponent')
async def fire_opponent_api(request: AddShipParams):
    response = fire_opponent(vars(request))

    return JSONResponse(
        status_code = 200,
        content = response
    )