from fastapi import APIRouter

from controllers import sensor_data

router = APIRouter()

router.include_router(sensor_data.sensor_router, prefix="/sensor-data")
