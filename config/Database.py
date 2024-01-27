from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from config.Enviroment import get_env

# Get enviroment variables
env = get_env()

# Get database url
DATABASE_URL = f"{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOST}"

# Create engine
engine = create_engine(DATABASE_URL, echo=env.DEBUG_MODE)

# Create session
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()