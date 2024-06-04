from .. import Base
from sqlalchemy.orm import Mapped, mapped_column


class Search(Base):
    __tablename__ = "searchings"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    subtext: Mapped[str]
