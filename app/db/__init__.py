from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine("sqlite:///my_db.db", echo=True)
Session = sessionmaker(engine)


class Base(DeclarativeBase): ...


from .models import Search
