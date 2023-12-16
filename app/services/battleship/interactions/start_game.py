from app.services.battleship.models.battlefield import BattleField
from app.services.battleship.shared_data import global_data


def start_game(request: dict):
    game = BattleField(field_size = request.get("field_size"))
    global_data[game.field_id] = game

    print("Welcome to Battleship!\n")

    return f"This is your game id: {game.field_id}"