from waffledotcom.src.database.models.base import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String


class DummyModel(DeclarativeBase):
    """Model for demo purpose."""

    __tablename__ = "dummy_model"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=200), unique=True)  # noqa: WPS432