from fastapi import HTTPException
from app.services.battleship.shared_data import global_data


def view_battle_field(request: dict):
    field_id = request.get("field_id")

    if not global_data.get(field_id):
        raise HTTPException(
            status_code = 400,
            detail = f"Battle Field does not exist with this field id"
        )
    
    field = global_data[field_id]

    half = field.field_size // 2

    print("Player A Battle Field\n")

    for i in range(0,half,1):
        print(field.battle_field[i])

    print("Player B Battle Field\n")

    for i in range(half,field.field_size,1):
        print(field.battle_field[i])