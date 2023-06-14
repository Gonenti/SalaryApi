from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
import itertools
from src.auth.base_config import fastapi_users
from src.auth.models import User
from src.database import get_async_session
from src.salary.models import salary
from src.auth.models import user
from src.salary.schemas import SalaryCreate

router = APIRouter(
    prefix="/salaries",
    tags=["Salary"]
)

current_user = fastapi_users.current_user()

@router.post("/insert_salary")
async def insert_salary(Salary_data: SalaryCreate,
                        user: User = Depends(current_user),
                        session: AsyncSession = Depends(get_async_session)):
    if (user.is_superuser == True):
        statement = insert(salary).values(**Salary_data.dict())
        await session.execute(statement)
        await session.commit()
        return {"status": "success"}
    else:
        raise HTTPException(status_code=403, detail="access denied")
    


@router.post("/get_salary")
async def get_salary_for_curent_user(user: User = Depends(current_user),
                            session: AsyncSession = Depends(get_async_session)):

    query = select(salary).where(salary.c.user_id == user.id)
    result = await session.execute(query)
    result = result.one()
    return {"user": user.userName, "amount": result[2], "increase_date":result[3], "payment_date":result[4]}