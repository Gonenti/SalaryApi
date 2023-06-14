from datetime import date
from pydantic import BaseModel


class SalaryCreate(BaseModel):
    id: int
    user_id: int
    value: int
    increase_date: date
    payment_date: date

class SalaryRead(BaseModel):
    id: int
    user_id: int
    value: int
    increase_date: date
    payment_date: date