from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base will translate OOP to database I believe
Base = declarative_base()
engine = create_engine("sqlite:///first_game.db", echo=False)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    import models
    
    Base.metadata.create_all(engine)
    print("Database initialized successfully!")