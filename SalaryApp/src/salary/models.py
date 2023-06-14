
from sqlalchemy import Table, Column, Integer, DateTime, MetaData, ForeignKey
from src.auth.models import user
metadata = MetaData()

salary = Table(
    "salary",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("value", Integer, nullable=False),
    Column("increase_date", DateTime, nullable=False),
    Column("payment_date", DateTime, nullable=False),
)
