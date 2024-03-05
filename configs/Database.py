from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from configs.Environment import get_env

# Get enviroment variables
env = get_env()

# Get database url
DATABASE_URL = f"{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"

# Create engine
engine = create_engine(DATABASE_URL, echo=env.DEBUG_MODE, future=True)

# Create session
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()