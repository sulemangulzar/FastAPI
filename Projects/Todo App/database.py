from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///todo.db"
engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)


def create_all_tables():
    SQLModel.metadata.create_all(bind=engine)


def get_session():
    with Session(engine) as session:
        yield session
