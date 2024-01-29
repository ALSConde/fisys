from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import Column, DateTime
from configs.Database import engine

# Base Entity Meta
EntityMeta = declarative_base()


# Initialize Data Model Attributes
def init():
    if not database_exists(engine.url):
        create_database(engine.url)
    
    EntityMeta.metadata.create_all(engine)

class BaseModel(EntityMeta):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
