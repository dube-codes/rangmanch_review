from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///rangmanch.db"

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    """Create all tables defind by SQLModel Class"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency that provides a database session per request"""
    with Session(engine) as session:
        yield session
