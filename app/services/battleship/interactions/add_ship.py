from fastapi import HTTPException
from app.services.battleship.models.ship import Ship
from app.services.battleship.shared_data import global_data


def add_ship(request: dict):
    field_id = request.get("field_id")

    if not global_data.get(field_id):
        raise HTTPException(
            status_code = 400,
            detail = f"Battle Field does not exist with this field id"
        )
    
    field = global_data[field_id]
    
    existing_ships = field.player_a_ships if request.get("player_id") == 'a' else field.player_b_ships

    check_validations(existing_ships, request)

    ship = Ship(request.get("x1"), request.get("y1"), request.get("x2"), request.get("y2"))

    existing_ships.append(ship)


def check_validations(existing_ships, request: dict):
    if len(existing_ships) >= 5:
        raise HTTPException(
            status_code = 400,
            detail = f"Maximum Number of ships reached for this player"
        )

    if overlapping(existing_ships, request):
        raise HTTPException(
            status_code = 400,
            detail = f"Ships are overlapping please try adding at other coordinates"
        )
    
def overlapping(ships: list, request: dict):
    x1 = request.get("x1")
    x2 = request.get("x2")
    y1 = request.get("y1")
    y2 = request.get("y2")

    return False

    # for ship in ships:
    #     if x1 >= ship.x1 and y1