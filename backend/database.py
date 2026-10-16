from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base will translate OOP to database I believe
Base = declarative_base()
DATABASE_URL = "sqlite:///first_game.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    import models
    
    Base.metadata.create_all(engine)
    print("Database initialized successfully!")