from database import Base, engine
import models

def init_database():
    print("Creating Database and tables!")
    Base.metadata.create_all(bind=engine)
    print("Initialization complete")

if __name__ == "__main__":
    init_database()