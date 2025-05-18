from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from dto.sensor_data import SensorDataIn, SensorDataOut
from models.sensor_data import SensorData
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select



sensor_router = APIRouter()


@sensor_router.get("")
def read_sensor():
    return {"message": "Hello, Sensor!!"}

@sensor_router.post("", status_code=status.HTTP_201_CREATED)
async def create(payload: SensorDataIn, db: AsyncSession = Depends(get_db)):
    new_data = SensorData(
        device_id=payload.device_id,
        timestamp=payload.timestamp,
        temperature=payload.temperature,
        humidity=payload.humidity,
    )

    try:
        db.add(new_data)
        await db.commit()
        await db.refresh(new_data)
        return {"id": new_data.id, "message": "Sensor data created successfully."}
    except SQLAlchemyError as e:
        print(e)
        await db.rollback()
        raise HTTPException(status_code=400, detail="Please try again")

@sensor_router.get("/{device_id}", response_model=List[SensorDataOut])
async def get_latest(device_id: str, db: AsyncSession = Depends(get_db)):
    query = (
        select(SensorData)
        .where(SensorData.device_id == device_id)
        .order_by(SensorData.timestamp.desc())
        .limit(5)
    )
    result = await db.execute(query)
    data = result.scalars().all()
    return data
