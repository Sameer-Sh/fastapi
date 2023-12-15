import os
from dotenv import load_dotenv
 
load_dotenv()
 
APP_ENV = os.environ.get("APP_ENV", "development")
APP_NAME = os.environ.get("APP_NAME", "project")
SHOW_DOCS_ENVIRONMENT = ["development", "staging"]

if APP_ENV in SHOW_DOCS_ENVIRONMENT:
    APP_CONFIGS = {
        "title": APP_NAME.replace("-", " ").title(),
        "openapi_url": f"/openapi.json",
        "docs_url": f"/docs",
        "description": "For Python FastAPI Project!",
    }
else:
    APP_CONFIGS = {}


POSTGRES_USER = os.environ.get("POSTGRES_USER", "root")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "root")
POSTGRES_HOST = os.environ.get("DATABASE_URL", "127.0.0.1")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")
POSTGRES_DATABASE_NAME = os.environ.get("POSTGRES_DATABASE_NAME", "test")