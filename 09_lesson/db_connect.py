from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASS = "qwerty123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = (f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}"
                f":{DB_PORT}/{DB_NAME}")

engine = create_engine(DATABASE_URL)
