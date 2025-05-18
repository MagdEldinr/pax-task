
from sqlalchemy import Column, Integer, String, Float, DateTime
from db import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True)
    device_id = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True))
    temperature = Column(Float)
    humidity = Column(Float)
