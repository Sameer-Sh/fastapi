from app.core import config
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
 
 
POSTGRES_URL = f"postgres://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DATABASE_NAME}"
 
 
TORTOISE_ORM = {
    "connections": {"default": POSTGRES_URL},
    "apps": {
        "pg_models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
 
 
def init_pg_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=POSTGRES_URL,
        modules={"pg_models": ["models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
