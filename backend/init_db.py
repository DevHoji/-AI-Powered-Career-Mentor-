from database import engine
from models import Base

def init_database():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("Initializing database...")
    init_database()
    print("Database initialized successfully!")
